from transformers import BartTokenizer, BartForConditionalGeneration
print("BART INITIALIZED")
# Load the BART model and tokenizer
model_name = "facebook/bart-large-cnn"

print("TOKENIZER LOADING....")
tokenizer = BartTokenizer.from_pretrained(model_name)
print("TOKENIZER LOADED")
print("MODEL LOADING....")
model = BartForConditionalGeneration.from_pretrained(model_name)
print("MODEL LOADED")


def bartSummarize_dict(input_dict):
    """
    Summarizes each value in the input dictionary and returns a new dictionary with summaries.

    Args:
    - input_dict (dict): A dictionary containing keys and corresponding values as strings.

    Returns:
    - dict: A new dictionary with keys unchanged and values replaced by their summaries.
    """
    summarized_dict = {}

    # Iterate over each key-value pair in the input dictionary
    for key, value in input_dict.items():
        # Tokenize the value (paper text)
        print('TOKENIZING INPUT')
        inputs = tokenizer.encode_plus(value, return_tensors="pt", max_length=1024, truncation=True)
        print("INPUT TOKENIZED")
        print("ENCODING.... ")
        # Generate summary
        summary_ids = model.generate(inputs["input_ids"], max_length=250, min_length=150, length_penalty=2.0,
                                     num_beams=5, early_stopping=True)
        print("ENCODED")
        print("DECODING....")
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        print("DECODED")
        # Store the summary in the new dictionary with the same key
        summarized_dict[key] = summary

    return summarized_dict
