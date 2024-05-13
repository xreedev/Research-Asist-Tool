from flask import Flask, request, jsonify
from flask_cors import CORS  # Add this line
import TFIDF as TI  # Module for TF IDF algorithm
import data as DT  # Module for retrieving data for processing
import webcrawler as PE  # Module for extracting data from PDF
import BART as BRT  # Module for summarizing data using BART model
import tts as TS  # Module for converting text to speech

app = Flask(__name__)
CORS(app)  # Add this line

stop_words = DT.stop_words  # this contains non-important terms to be removed

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    print(data)
    url = data['url']

    dataset = PE.extract_article_sections(url)  # extract content from pdf
    if 'Title' in dataset:
        title = dataset['Title']
    else:
        title = ""

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
    Summarized_data = BRT.bartSummarize_dict(Summarized_data_TFIDF)  # BART SUMMARIZATION
    for key in Summarized_data.keys():
        print(key, Summarized_data[key].split("."))
    TS.texttospeech(Summarized_data, "female")  # convert text to audio file

    return jsonify(Summarized_data)

if __name__ == '__main__':
    app.run(debug=True)
