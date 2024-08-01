
---

# Research Assist Tool

## Overview

Research Assist Tool simplifies and summarizes scientific data, converts it into audio podcasts, and creates PowerPoint presentations. Ideal for researchers, academics, and students.

## Features

- **Automated Text Mining**: Extracts relevant segments using the TF-IDF algorithm.
- **Content Generation**: Summarizes with BART model.
- **PowerPoint Presentation**: Creates slides with Python pptx.
- **Text-to-Speech**: Converts summaries to audio using VidLab API.

## Setup

1. **Clone Repository**:
    ```sh
    git clone https://github.com/xreedev/Research-Asist-Tool.git
    ```
2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
3. **Start Backend API**:
    ```sh
    python app.py
    ```
4. **Run Frontend**:
    ```sh
    npm install
    cd Frontend
    npm start
    ```

## Usage

1. **Pre-trained Models**: Download and configure BART models.
2. **Summarization**: Provide the link through the React website.
3. **Output**: Access summaries, presentations, and audio files in the `Outputs` folder.

---

## File Structure

```
Research-Asist-Tool/
│
├── app.py                     # Backend API script
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
│
├── Frontend/                  # Frontend files
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   ├── index.js           # Entry point for React
│   │   ├── components/        # React components
│   │   ├── services/          # API service functions
│   │   └── styles/            # CSS files
│   ├── public/
│   │   ├── index.html         # Main HTML file
│   │   └── ...
│   └── package.json           # Node.js dependencies
│
├── Models/                    # Pre-trained models
│   ├── bart/                  # BART models
│   ├── tf-idf/                # TF-IDF models
│   └── ...
│
├── Outputs/                   # Generated outputs
│   ├── summaries/             # Text summaries
│   ├── presentations/         # PowerPoint files
│   └── audio/                 # Audio files
│
└── Utils/                     # Utility scripts
    ├── text_mining.py         # Text mining functions
    ├── summarization.py       # Summarization functions
    ├── ppt_creation.py        # PowerPoint generation
    └── text_to_speech.py      # Text-to-speech conversion
```

## Data Flow

1. **Text Mining**:
    - **Input**: Scientific paper (PDF/URL)
    - **Process**: Extracts key segments using `text_mining.py`
    - **Output**: Relevant text segments

2. **Summarization**:
    - **Input**: Extracted text segments
    - **Process**: Summarizes using BART model (`summarization.py`)
    - **Output**: Summarized text

3. **PowerPoint Creation**:
    - **Input**: Summarized text
    - **Process**: Generates slides using `ppt_creation.py`
    - **Output**: PowerPoint file

4. **Text-to-Speech**:
    - **Input**: Summarized text
    - **Process**: Converts to audio using `text_to_speech.py`
    - **Output**: Audio file

## Contribution

- Jafar N
- Sharon T Saju
- Sreedev TS (xreedev@gmail.com)

## License

Licensed under the MIT License. See [LICENSE](link-to-license-file) for details.

---
