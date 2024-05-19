import os
import requests
#you can redisgn this module to use any api you want
#the input to this module is a dictionary and output is all the values in dictionary appended and converted to audio
def texttospeech(Summarized_data, reqd):
    print("tts on")
    url = "https://realistic-text-to-speech.p.rapidapi.com/v3/generate_voice_over_v2"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "f6b9f7e5a3mshc27a2083997f30fp1d3f5djsnd9b63dcb026b",
        "X-RapidAPI-Host": "realistic-text-to-speech.p.rapidapi.com"
    }
    audio_paths = []

    # Iterate over each section in Summarized_data
    for section_title, section_content in Summarized_data.items():
        payload = {
            "voice_obj": {
                "id": 2014 if reqd == "male" else 2009,
                "voice_id": "en-US-Neural2-A" if reqd == "male" else "en-GB-Neural2-A",
                "gender": "Male" if reqd == "male" else "Female",
                "language_code": "en-US" if reqd == "male" else "en-GB",
                "language_name": "US English" if reqd == "male" else "British English",
                "voice_name": "John" if reqd == "male" else "Charlotte",
                "sample_text": "Hello, hope you are having a great time making your video.",
                "sample_audio_url": "https://s3.ap-south-1.amazonaws.com/invideo-uploads-ap-south-1/speechen-US-Neural2-A16831901130600.mp3" if reqd == "male" else "https://s3.ap-south-1.amazonaws.com/invideo-uploads-ap-south-1/speechen-GB-Neural2-A16831903682720.mp3",
                "status": 2,
                "rank": 0,
                "type": "google_tts",
                "isPlaying": False
            },
            "json_data": [
                {
                    "block_index": 0,
                    "text": section_content  # Use section_content for current section
                }
            ]
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.ok:
            link = response.json()[0]["link"]
            resp = requests.get(link)
            audio_paths.append(resp.content)
        else:
            print(f"Error in {reqd} voice request for {section_title}:", response.text)

    return audio_paths

def combine_audio_files(audio_paths, output_file):
    with open(output_file, "wb") as output:
        for audio_data in audio_paths:
            output.write(audio_data)

# Test the function
# Summarized_data = {
#     "INTRODUCTION": "This is the introduction. It provides an overview of the topic.",
#     "ABSTRACT": "This is the abstract. It summarizes the main points of the research.",
#     "METHOD": "This section outlines the methodology used in the research process.",
#     "RESULTS": "Here are the results obtained from the research analysis.",
#     "DISCUSSION": "This section discusses the implications and interpretations of the results.",
#     "CONCLUSION": "In conclusion, the research findings are summarized and final remarks are provided.",
#     "DATA_ANALYSIS": "Data analysis involves examining, cleaning, transforming, and modeling data to discover useful information, inform conclusions, and support decision-making.",
#     "REFERENCES": "References provide details of the sources cited in the research paper, allowing readers to locate the original works."
# }
# audio_data = texttospeech(Summarized_data, "female")  # Convert text to audio files
# combine_audio_files(audio_data, "Outputs\\combined_audio.mp3")  # Combine audio files into one
