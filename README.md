
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
- python app.py to start python backend api
- cd frontend
- npm start to open website

### Pre-trained Models:

- Download pre-trained BART models and configure the transformers library accordingly.

### Summarization:

- Run the summarization script, by providing the link through the React website.

### Output:

- View the  generated Summary , PowerPoint presentation (summary.pptx) containing the summarized content as well as audio file (audio.mp3).

## Contribution:

- Jafar N
- Sharon T Saju
- Sreedev TS

## License:

This project is licensed under the MIT License. See the LICENSE file for details.

---

This updated README provides users with information about the Text-to-Speech feature integrated into the Scientific Paper Summarizer tool. Adjustments have been made to remove the example code and provide a clear overview of the tool's capabilities. Feel free to further customize the content to suit your project's requirements.
