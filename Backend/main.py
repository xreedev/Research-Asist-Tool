import ppt as PT  # Module for PPT generation
import TFIDF as TI  # Module for TF IDF algorithm
import data as DT  # Module for retrieving data for processing
import tts as TS  # Module for converting text to speech
import webcrawler as PE  # Module for extracting data from PDF
import BART as BRT  # Module for summarizing data using BART model
stop_words = DT.stop_words  # this contains non-important terms to be removed

dataset = PE.extract_article_sections("https://fbj.springeropen.com/articles/10.1186/s43093-024-00326-4")  # extract content from pdf)


dataset.pop('Title')
Summarized_data_TFIDF = TI.tfidfVectorise(dataset, DT.stop_words, 0.35)  # TF IDF SUMMARIZATION
print("TF IDF DONE")
for key in Summarized_data_TFIDF.keys():
    if Summarized_data_TFIDF[key]=="":
      blank=key
Summarized_data_TFIDF.pop(blank)
Summarized_data = BRT.bartSummarize_dict(Summarized_data_TFIDF)  # BART SUMMARIZATION
for key in Summarized_data.keys():
    print(key,Summarized_data[key].split("."))
TS.texttospeech(Summarized_data,"female")  # convert text to audio file
PT.save_ppt("template.pptx", Summarized_data,"--TITLE--", DT.author_list)