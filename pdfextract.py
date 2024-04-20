import fitz
import re
def getcontent(sample):
    doc = fitz.open(sample)

    # Extract text and clean it
    cleaned_text = ""
    for page in doc:
        text = page.get_text()
        cleaned_text += text
print("text")