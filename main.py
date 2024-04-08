import dataProcesser as DP
import TFIDF as TI
import data
import BART as BRT
# import BART as SB


ieee_paper_data = data.ieee_paper_data  # contents of scientific paper
stop_words = data.stop_words  # this contains non-important terms to be removed

classified_dataset = DP.classify(ieee_paper_data)  # classified data
clean_dataset = DP.cleanData(ieee_paper_data, stop_words)  # classified data without stopwords
lines = DP.getAllLines(ieee_paper_data)

# Ask the user for their choice of summarization
summarization_choice =0
Summarized_data = TI.tfidfVectorise(classified_dataset, lines, data.stop_words, 0.5)


print(BRT.bertSummarize_dict(Summarized_data))



