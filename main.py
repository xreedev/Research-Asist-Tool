import dataProcesser as DP
import TFIDF as TI


ieee_paper_data = """
1. Introduction
Artificial intelligence (AI) has emerged as a transformative technology in various fields, including healthcare, finance, manufacturing, and transportation. 
Its ability to analyze large volumes of data and extract valuable insights has revolutionized decision-making processes and led to significant advancements in automation and efficiency.
However, despite its tremendous potential, AI systems often face challenges related to bias, interpretability, and scalability,which need to be addressed to ensure their responsible deployment and widespread adoption.

2. Related Work
Prior research in the field of AI has explored various techniques for machine learning and data analysis. 
Traditional approaches include support vector machines (SVMs), decision trees, and k-nearest neighbors (KNN).
More recently, deep learning methods, such as convolutional neural networks (CNNs) and recurrent neural networks (RNNs), have shown superior performance in tasks such as image recognition, natural language processing, and speech recognition.
However, these models often require large amounts of labeled data and computational resources, limiting their applicability in resource-constrained environments.

3. Methodology
In this study, we propose a novel approach for sentiment analysis using deep learning techniques.
The methodology consists of preprocessing the text data, including tokenization, stemming, and vectorization, followed by training a long short-term memory (LSTM) network for sentiment classification.
We evaluate the model using standard performance metrics, such as accuracy, precision, recall,and F1-score, on benchmark datasets such as IMDb movie reviews and Twitter sentiment analysis dataset.

4. Results
Our experiments demonstrate that the proposed LSTM-based model outperforms baseline methods in sentiment classification tasks.
We achieve an accuracy of over 90% on both the IMDb and Twitter datasets, highlighting the effectiveness of deep learning for natural language understanding.
Additionally, we conduct ablation studies to analyze the impact of different components of the model architecture on performance.

5. Discussion
The results indicate that the LSTM network effectively captures long-range dependencies in text sequences, enabling it to discern subtle nuances in sentiment expression.
However, challenges remain in handling noisy and ambiguous language, especially in user-generated content on social media platforms.
Future research directions include exploring advanced architectures, such as attention mechanisms and transformer models, for improved sentiment analysis performance.

6. Conclusion
In conclusion, our study presents a comprehensive analysis of sentiment analysis using deep learning techniques. 
The proposed LSTM-based model demonstrates promising results in accurately classifying sentiment in text data. 
By addressing key challenges and exploring innovative solutions, we can further enhance the capabilities of AI systems for natural language understanding and enable applications in areas such as customer feedback analysis,market sentiment prediction, and opinion mining.
"""

classified_data=DP.getClassifiedData(ieee_paper_data) #This is the data classified on basis of various sections
#print(classified_data[0])
#print(DP.sections) #This shows the content at various indexes of classified_data



classified_data={"Introduction":classified_data[0],"Related Work":classified_data[1],"Methodology":classified_data[2],"Discussion":classified_data[3],"Conclusion":classified_data[4]}
#print(classified_data)

Summarized_data=TI.tfidfVector(ieee_paper_data,classified_data,DP.getAllLines(ieee_paper_data))
print(Summarized_data["Related Work"])