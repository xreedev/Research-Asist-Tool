import dataProcesser as DP
import TFIDF as TI
import data
import BERT as SB

ieee_paper_data = data.ieee_paper_data  # contents of scientific paper
stop_words = data.stop_words  # this contains non-important terms to be removed

classified_dataset = DP.classify(ieee_paper_data)  # classified data
clean_dataset = DP.cleanData(ieee_paper_data, stop_words)  # classified data without stopwords
lines = DP.getAllLines(ieee_paper_data)

# Ask the user for their choice of summarization
summarization_choice =0


while(summarization_choice!=3):
    summarization_choice = input("Choose a summarization method (1 for TF-IDF, 2 for BERT,3 for exit): ")
    if summarization_choice == '1':
        # Vectorize the text using TF-IDF Algorithm
        Summarized_data = TI.tfidfVectorise(classified_dataset, lines, data.stop_words, 1.9)
        print(Summarized_data)
    elif summarization_choice == '2':
        # Summarize using BERT
        Summarized_paper = SB.bertSummarize(ieee_paper_data)
        print(Summarized_paper)
