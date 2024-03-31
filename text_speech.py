import pyttsx3

def text_to_speech_with_highlight(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech

    # Convert the entire text to speech
    engine.say(text)
    engine.runAndWait()
