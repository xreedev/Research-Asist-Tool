import PyPDF2

def pdf_to_text(pdf_path):
    sentence_list = []
    text = ""
    file = open(pdf_path, "rb")
    try:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            # Extract text from the page
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        # Split text into sentences
        sentence_list = text.split("\n")
        abstract_start_index = 0
        for i in range(len(text)):
            if "Abstract" in text[i]:
                abstract_start_index = i
                break
        if abstract_start_index !=0:
            abstract = ""
            for i in range(abstract_start_index + 1, len(text)):
                if text[i].strip():
                    abstract += text[i] + " "
                else:
                    break
            abstract = abstract.strip()
        else:
            abstract = ""
    finally:
        file.close()

    return sentence_list,abstract
