from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import TFIDF as TI  # Module for TF IDF algorithm
import data as DT  # Module for retrieving data for processing
import webcrawler as PE  # Module for extracting data from PDF
import BART as BRT  # Module for summarizing data using BART model
import tts as TS  # Module for converting text to speech
import ppt as PT  # Module for PPT generation
import os

app = Flask(__name__)
CORS(app)  # Add this line

# stop_words = DT.stop_words  # this contains non-important terms to be removed

@app.route('/summarize', methods=['POST'])
def summarize():
    # Summarized_data = {
    #     "INTRODUCTION": "This is the introduction. It provides an overview of the topic.",
    #     "ABSTRACT": "This is the abstract. It summarizes the main points of the research.",
    #     "METHOD": "This section outlines the methodology used in the research process.",
    #     "RESULTS": "Here are the results obtained from the research analysis.",
    #     "DISCUSSION": "This section discusses the implications and interpretations of the results.",
    #     "CONCLUSION": "In conclusion, the research findings are summarized and final remarks are provided.",
    #     "DATA_ANALYSIS": "Data analysis involves examining, cleaning, transforming, and modeling data to discover useful information, inform conclusions, and support decision-making.",
    #     "REFERENCES": "References provide details of the sources cited in the research paper, allowing readers to locate the original works."
    # }
    data = request.get_json()
    url = data['url']

    dataset = PE.extract_article_sections(url)  # extract content from pdf
    keys_to_remove = []
    string_to_check = "AUTHOR"

    for key in dataset.keys():
        if string_to_check in key:
            keys_to_remove.append(key)

    for key in keys_to_remove:
        dataset.pop(key)

    dataset.pop('Title')
    Summarized_data_TFIDF = TI.tfidfVectorise(dataset, DT.stop_words, 0.35)  # TF IDF SUMMARIZATION

    for key in Summarized_data_TFIDF.keys():
        if Summarized_data_TFIDF[key] == "":
            blank = key
    Summarized_data_TFIDF.pop(blank)
    Summarized_data_TFIDF.pop("ABSTRACT")
    Summarized_data_TFIDF.pop("INTRODUCTION")
    Summarized_data_TFIDF.pop("CONCLUSION")
    Summarized_data_TFIDF.pop("RESULTS")
    Summarized_data = BRT.bartSummarize_dict(Summarized_data_TFIDF)  # BART SUMMARIZATION

    audio_data = TS.texttospeech(Summarized_data, "female")  # convert text to audio file
    TS.combine_audio_files(audio_data, "Outputs/combined_audio.mp3")
    PT.save_ppt("template.pptx", Summarized_data, "--TITLE--", DT.author_list)

    return jsonify(Summarized_data)

@app.route('/download_ppt', methods=['GET'])
def download_ppt():
    path = "Outputs/new.pptx"
    return send_file(path, as_attachment=True)

@app.route('/download_audio', methods=['GET'])
def download_audio():
    path = "Outputs/combined_audio.mp3"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
