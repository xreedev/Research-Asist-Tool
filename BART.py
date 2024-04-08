from transformers import BartTokenizer, BartForConditionalGeneration

# Load the BART model and tokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)
def bertSummarize(paper_text):



    # Tokenize the paper text
    inputs = tokenizer.encode_plus(paper_text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs["input_ids"], max_length=1050, min_length=250, length_penalty=2.0, num_beams=4,early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Print the summary

    return summary
ieee_paper_text=ieee_paper_data = """
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
print(bertSummarize(ieee_paper_text))