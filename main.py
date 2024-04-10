import ppt as PT # Module for PPT generation
import dataProcesser as DP  # Module for preprocessing data
import TFIDF as TI # Module for TF IDF algorithm
import data as DT # Module for retrieving data for processing
import tts as TS
# import BART as BRT # Module for BART summarization

ieee_paper_data = DT.ieee_paper_data  # contents of scientific paper
stop_words = DT.stop_words  # this contains non-important terms to be removed

classified_dataset = DP.classify(ieee_paper_data)  # classified data
clean_dataset = DP.cleanData(ieee_paper_data, stop_words)  # classified data without stopwords

Summarized_data = TI.tfidfVectorise(classified_dataset, DP.getAllLines(ieee_paper_data), DT.stop_words, 0.5) # TF IDF SUMMARIZATION
text=""
for values in Summarized_data.values():
    text += values
print(text)
TS.texttospeech(text,"female")


# PT.save_ppt("template.pptx",BRT.bartSummarize_dict(Summarized_data),"ARTIFICIAL INTELLIGENCE",DT.author_list) # BART SUMMARIZATION




