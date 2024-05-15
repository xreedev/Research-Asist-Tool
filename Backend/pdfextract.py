import fitz
import re

doc = fitz.open("sample.pdf")
# Extract text and clean it
cleaned_text = ""
page=doc[1]
text = page.get_text()
cleaned_text += text
print(cleaned_text)