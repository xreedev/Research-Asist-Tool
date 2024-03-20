import PyPDF2

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            # Extract text from the page
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text
