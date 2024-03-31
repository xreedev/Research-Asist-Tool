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