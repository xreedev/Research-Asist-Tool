from transformers import BartTokenizer, BartForConditionalGeneration

# Load the BART model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)


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
        inputs = tokenizer.encode_plus(value, return_tensors="pt", max_length=1024, truncation=True)

        # Generate summary
        summary_ids = model.generate(inputs["input_ids"], max_length=250, min_length=50, length_penalty=2.0,
                                     num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        # Store the summary in the new dictionary with the same key
        summarized_dict[key] = summary

    return summarized_dict


