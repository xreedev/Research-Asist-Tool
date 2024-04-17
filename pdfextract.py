import fitz  # PyMuPDF
import re

# Function to clean text
def clean_text(text):
    cleaned_text = ""
    pattern_unwanted = r'[!?*+&\"#$\)*)+,\%-*+,/$\'\(\)*$]|'
    pattern_number = r'(\n\d+\n|\[\d+\]|\n\d+\n|-\d+\.\d+|\d+\.\d+|-\d+)'
    pattern_blank = r'\n\s*\n'
    cleaned_text1 = re.sub(pattern_unwanted, '', text)
    cleaned_text2 = re.sub(pattern_number, '', cleaned_text1)
    cleaned_text = re.sub(pattern_blank, '', cleaned_text2)
    return cleaned_text

# Function to categorize sections
def categorize_sections(text, headings):
    sections = {}
    # Initialize starting index for each section
    start_index = 0
    # Iterate over headings
    for i, (roman_numeral, heading) in enumerate(headings):
        # Find the start index of the current heading
        start_index = text.find(heading, start_index)
        if start_index == -1:
            # If heading not found, break
            break
        # Find the end index of the current section
        end_index = len(text)
        if i < len(headings) - 1:
            # Find the start index of the next heading
            next_start_index = text.find(headings[i + 1][1], start_index)
            if next_start_index != -1:
                end_index = next_start_index
        # Extract the section text
        section_text = text[start_index:end_index].strip()
        # Add section to dictionary
        sections[heading] = section_text
        # Update start index for next section
        start_index = end_index
    return sections

def getcontent(sample):
    doc = fitz.open(sample)

    # Extract text and clean it
    cleaned_text = ""
    for page in doc:
        text = page.get_text()
        cleaned_text += clean_text(text)
    heading_pattern = r'\n([IVXL]+).\n([^\n]+)\n'

    # Find all occurrences of headings in the text
    headings = re.findall(heading_pattern, cleaned_text)

    # Categorize sections
    sections = categorize_sections(cleaned_text, headings)
    # for key in sections.keys():
    #     # new_text=sections[key].replace("\n","")
    #     lines = sections[key].split("\n")
    #     sections[key] = lines
    # for line in sections["INTRODUCTION"]:
    #     print(line)
    return sections

