import fitz
import re


def categorize_sections(pdf_file):
    sections = {
        "ABSTRACT": "",
        "INTRODUCTION": "",
        "METHODOLOGY OF RESEARCH": "",
        "BACKGROUND OF RESEARCH": "",
        "CONCLUSION": "",
        "FUTURE DIRECTIONS": "",
        "REFERENCES": ""
    }

    # Regular expression pattern to match the headings
    heading_pattern = r'\b(?:ABSTRACT|INTRODUCTION|METHODOLOGY OF RESEARCH|BACKGROUND OF RESEARCH|CONCLUSION|FUTURE DIRECTIONS|REFERENCES)\b'

    doc = fitz.open(pdf_file)

    # Compile the regular expression pattern
    regex = re.compile(heading_pattern)

    # Iterate through each page in the document
    for page in doc:
        # Extract text from the page
        text = page.get_text()

        # Find all matches of the heading pattern in the text
        matches = regex.finditer(text)

        # Iterate through matches to extract text between headings
        start = None
        for match in matches:
            if start is not None:
                # Extract text between the current and previous heading
                section_text = text[start:match.start()].strip()
                # Assign the extracted text to the corresponding section
                sections[heading] += section_text + "\n"

            # Update the start position to the end of the current heading
            start = match.end()
            # Get the heading from the current match
            heading = match.group()

        # Extract text from the last heading to the end of the page
        if start is not None:
            section_text = text[start:].strip()
            sections[heading] += section_text + "\n"

    # Close the PDF document
    doc.close()

    return sections


# Example usage:
pdf_file = "sample.pdf"
sections = categorize_sections(pdf_file)
print("Sections extracted from the PDF:")
for heading, text in sections.items():
    print(f"--- {heading} ---")
    print(text)
