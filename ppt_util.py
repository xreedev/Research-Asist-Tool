from transformers import pipeline


def summarize_text(text, max_length=150):
    # Initialize the summarization pipeline
    summarization_pipeline = pipeline("summarization")

    # Generate summary
    summary = summarization_pipeline(text, max_length=max_length)

    return summary[0]['summary_text']


# Example text
text = """
If you're not seeing any visible output when running your code, it's possible that the code is executing without errors but not displaying any output explicitly. Here are a few things you can check and try:
1. Print Statements: Add print statements to see the output of your code explicitly.
2. Verify Model Loading: Check if the model and tokenizer are loaded correctly without any errors.
3. Execution Environment: Ensure that your code is running in an environment where you can see the output.
4. Inspect Variables: Inspect the variables in your code to see if they contain the expected values.
5. Dependencies: Double-check that all dependencies are installed correctly and up-to-date.
"""

# Summarize text
summary = summarize_text(text)
print(summary)
