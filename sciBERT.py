from transformers import BartTokenizer, BartForConditionalGeneration

# Load the BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Sample scientific paper text
paper_text = """
            In recent years, natural language processing (NLP) has seen tremendous advancements, driven largely by deep learning techniques. In this paper, we explore the use of SciBERT, a variant of BERT pre-trained on scientific text, for summarizing scientific papers.

            We conduct experiments on a dataset comprising research articles from various domains, including biology, physics, and computer science. Our approach involves tokenizing the input text and passing it through the SciBERT model to obtain contextualized representations.

            The experimental results demonstrate that SciBERT is effective in capturing the key information from scientific papers. We compare the performance of SciBERT-based summarization with traditional techniques such as TF-IDF and find that SciBERT outperforms them in terms of both extractive and abstractive summarization.

            Furthermore, we analyze the impact of fine-tuning SciBERT on the summarization task. By fine-tuning SciBERT on a labeled dataset for summarization, we achieve even better performance, indicating the potential for further improvements through task-specific adaptation.

            Overall, our findings suggest that SciBERT holds promise for automating the summarization of scientific papers, offering researchers a valuable tool for quickly extracting relevant information from large volumes of scholarly literature.
            """


# Tokenize the paper text
inputs = tokenizer.encode_plus(paper_text, return_tensors="pt", max_length=1024, truncation=True)

# Generate summary
summary_ids = model.generate(inputs["input_ids"], max_length=1050, min_length=250, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print("Summary:", summary)


