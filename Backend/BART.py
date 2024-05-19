from transformers import BartTokenizer, BartForConditionalGeneration
import os

# Define the paths for saving/loading tokenizer and model
#the input to this module is a dictionary and output is all the abstractive summaries of values in dictionary
tokenizer_path = "bart_tokenizer"
model_path = "bart_model"

if os.path.exists(tokenizer_path) and os.path.exists(model_path):
    # Load the tokenizer and model from the saved files
    print("Loading tokenizer and model from saved files...")
    tokenizer = BartTokenizer.from_pretrained(tokenizer_path)
    model = BartForConditionalGeneration.from_pretrained(model_path)
else:
    # Load the BART model and tokenizer
    print("Initializing BART model and tokenizer...")
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)

    # Save the tokenizer and model for future use
    tokenizer.save_pretrained(tokenizer_path)
    model.save_pretrained(model_path)

print("BART initialized")


def bartSummarize_dict(input_dict):
    summarized_dict = {}

    # Iterate over each key-value pair in the input dictionary
    for key, value in input_dict.items():
        # Tokenize the value (paper text)
        inputs = tokenizer.encode_plus(value, return_tensors="pt", max_length=1024, truncation=True)
        print("INPUT TOKENIZED")
        # Generate summary
        summary_ids = model.generate(inputs["input_ids"], max_length=250, min_length=150, length_penalty=2.0,
                                     num_beams=5, early_stopping=True)
        print("ENCODED")
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print("DECODED")
        # Store the summary in the new dictionary with the same key
        summarized_dict[key] = summary

    return summarized_dict
