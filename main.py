import ppt as PT  # Module for PPT generation
import TFIDF as TI  # Module for TF IDF algorithm
import data as DT  # Module for retrieving data for processing
import tts as TS  # Module for converting text to speech
import pdfextract as PE  # Module for extracting data from PDF
import BART as BRT  # Module for summarizing data using BART model
stop_words = DT.stop_words  # this contains non-important terms to be removed

dataset = PE.getcontent("sample.pdf")  # extract content from pdf

Summarized_data_TFIDF = TI.tfidfVectorise(dataset, DT.stop_words, 0.7)  # TF IDF SUMMARIZATION
print("TF IDF DONE")
Summarized_data = BRT.bartSummarize_dict(Summarized_data_TFIDF)  # BART SUMMARIZATION
for key in Summarized_data["INTRODUCTION"].split("."):
    print(key)
# TS.texttospeech(Summarized_data, "female")  # convert text to audio file
#
# # Create Presentation
# PT.save_ppt("template.pptx", BRT.bartSummarize_dict(Summarized_data), "ARTIFICIAL INTELLIGENCE", DT.author_list)
