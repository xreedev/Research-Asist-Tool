import dataProcesser as DP
import TFIDF as TI
import data
import sciBERT as SB

ieee_paper_data=data.ieee_paper_data # contents of scientific paper
stop_words=data.stop_words # this contains non-important terms to be removed

classified_dataset = DP.classify(ieee_paper_data)  # classified data
clean_dataset = DP.cleanData(ieee_paper_data,stop_words)  # classified data without stopwords
lines=DP.getAllLines(ieee_paper_data)

Summarized_data=TI.tfidfVectorise(classified_dataset,lines,data.stop_words,1.9) # Vectorise the text using TF-IDF Algorithm
Summarized_paper=SB.bertSummarize(ieee_paper_data)
print(Summarized_paper)
