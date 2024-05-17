
---

# Scientific Paper Summarizer and Research Assist

This website was designed to  help researchers and students help simplify understanding and working with
scientific articles and research papers.This tool currently only wokrs for Springr non-mathematical papers 
only.New versions will aim to add more papers and capabilities, all contributions are openly welcomed, in
building a student and research friendly application.

## Features:

- **Automated Text Mining**: Utilizes TF-IDF algorithm to extract relevant text segments from scientific papers.
- **Content Generation**: Employs BART (Bidirectional and Auto-Regressive Transformers) model for generating comprehensive summaries from mined text segments.
- **PowerPoint Presentation**: Integrates with the Python pptx library to create visually appealing PowerPoint slides containing the summarized content.
- **Text-to-Speech**: Incorporates the Realistic Text to Speech API by VidLab for converting text summaries into natural-sounding speech, enhancing accessibility and user experience.

## Usage:

### Setup:

- Clone the repository and install the required dependencies.
```
pip install -r requirements.txt
```
- To start python backend api
```
python app.py
```
- To run React website
```
cd Frontend
```
```
npm start
```

### Pre-trained Models:

- Download pre-trained BART models and configure the transformers library accordingly.

### Summarization:

- Run the summarization script, by providing the link through the React website.

### Output:

- View the  generated Summary , PowerPoint presentation (summary.pptx) containing the summarized content as well as audio file (audio.mp3).

The Outputs folder will contain all the non-text outputs
## Contribution:

- Jafar N
- Sharon T Saju
- Sreedev TS , xreedev@gmail.com

## Module Design

app.py : Flask api to treat requests
ppt.py : create ppt based on template.pptx
BART.py : Module responsible for summarization using BART
data.py :Used to store any data repetitively used
dataProcesser.py : Used to remove stop words
main.py:To test all backend features
pdfextract.py: Used to extract text from pdfs(incomplete)
TFIDF.py:Extractive summarization using TF-IDF algorithm
tts.py : Test to speech module
webcrawler.py:Webcrawl and parse data from springr articles


## License:

This project is licensed under the MIT License. See the LICENSE file for details.

---

