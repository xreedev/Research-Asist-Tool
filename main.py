import dataProcesser as DP
import TFIDF as TI
import data



ieee_paper_data=data.ieee_paper_data # contents of scientific paper
stop_words=data.stop_words # this contains non-important terms to be removed

classified_dataset = DP.classify(ieee_paper_data)  # classified data
clean_dataset = DP.cleanData(ieee_paper_data,stop_words)  # classified data without stopwords

Summarized_data=TI.tfidfVectorise(ieee_paper_data,clean_dataset,DP.getAllLines(ieee_paper_data),classified_dataset) # Vectorise the text using TF-IDF Algorithm
print(Summarized_data)
