import ppt as PT  # Module for PPT generation
import TFIDF as TI  # Module for TF IDF algorithm
import data as DT  # Module for retrieving data for processing
import tts as TS  # Module for converting text to speech
import webcrawler as PE  # Module for extracting data from PDF
import BART as BRT  # Module for summarizing data using BART model
stop_words = DT.stop_words  # this contains non-important terms to be removed

dataset = PE.extract_article_sections("https://fbj.springeropen.com/articles/10.1186/s43093-024-00326-4")  # extract content from pdf)
print(dataset.keys())
if 'Title' in dataset:
    title = dataset['Title']
else:
    title=""
keys_to_remove = []
string_to_check = "AUTHOR"

for key in dataset.keys():
    if string_to_check in key:
        keys_to_remove.append(key)
for key in keys_to_remove:
    dataset.pop(key)
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
# Create Presentation
# Summarized_data = {
#     "INTRODUCTION": "This is the introduction. This is the introduction.It provides an overview of the topic.",
#     "ABSTRACT": "This is the abstract.This is the abstract. It summarizes the main points of the research.",
#     "METHOD": "This is the abstract.This is the abstract.This section outlines the methodology used in the research process.",
#     "RESULTS": "This is the abstract.This is the abstract.Here are the results obtained from the research analysis.",
#     "DISCUSSION": "This is the abstract.This is the abstract.This section discusses the implications and interpretations of the results.",
#     "CONCLUSION": "This is the abstract.This is the abstract.In conclusion, the research findings are summarized and final remarks are provided.",
#     "DATA_ANALYSIS": "This is the abstract.Data analysis involves examining, cleaning, transforming, and modeling data to discover useful information, inform conclusions, and support decision-making.This is the abstract.",
#     "REFERENCES": "This is the abstract.References provide details of the sources cited in the research paper, allowing readers to locate the original works.This is the abstract."
# }
PT.save_ppt("template.pptx", Summarized_data,"--TITLE--", DT.author_list)