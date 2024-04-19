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

    # Extract meaningful sentences from each section
    for heading, section_text in sections.items():
        sections[heading] = extract_meaningful_sentences(section_text)

    # Combine sentences into paragraphs for each section
    for heading, sentences in sections.items():
        sections[heading] = ' '.join(sentences)

    return sections

# Usage
sample_pdf = "sample.pdf"
content = getcontent(sample_pdf)
for heading, paragraph in content.items():
    print(f"Section: {heading}")
    print(paragraph)
