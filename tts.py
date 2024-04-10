import requests
def texttospeech(Summarized_data,reqd):
	text = ""
	for values in Summarized_data.values():
		text += values

	url = "https://realistic-text-to-speech.p.rapidapi.com/v3/generate_voice_over_v2"

	payload = {
		"voice_obj": {
			"id": 2014,
			"voice_id": "en-US-Neural2-A",
			"gender": "Male",
			"language_code": "en-US",
			"language_name": "US English",
			"voice_name": "John",
			"sample_text": "Hello, hope you are having a great time making your video.",
			"sample_audio_url": "https://s3.ap-south-1.amazonaws.com/invideo-uploads-ap-south-1/speechen-US-Neural2-A16831901130600.mp3",
			"status": 2,
			"rank": 0,
			"type": "google_tts",
			"isPlaying": False
		},
		"json_data": [
			{
				"block_index": 0,
				"text": text
			}
		]
	}
	payload_female = {
		"voice_obj": {
			"id": 2009,
			"voice_id": "en-GB-Neural2-A",
			"gender": "Female",
			"language_code": "en-GB",
			"language_name": "British English",
			"voice_name": "Charlotte",
			"sample_text": "Hello, hope you are having a great time making your video.",
			"sample_audio_url": "https://s3.ap-south-1.amazonaws.com/invideo-uploads-ap-south-1/speechen-GB-Neural2-A16831903682720.mp3",
			"status": 2,
			"rank": 0,
			"type": "google_tts",
			"isPlaying": False
		},
		"json_data": [
			{
				"block_index": 0,
				"text": text
			}
		]
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "f6b9f7e5a3mshc27a2083997f30fp1d3f5djsnd9b63dcb026b",
		"X-RapidAPI-Host": "realistic-text-to-speech.p.rapidapi.com"
	}

	if reqd =="male":
		response_male = requests.post(url, json=payload, headers=headers)
		link_male = response_male.json()[0]["link"]

		resp_male = requests.get(link_male)
		open("Outputs//audio_male.mp3", "wb").write(resp_male.content)

	if reqd=="female":
		response_female = requests.post(url, json=payload_female, headers=headers)
		link_female = response_female.json()[0]["link"]

		resp_female = requests.get(link_female)
		open("Outputs//audio_female.mp3", "wb").write(resp_female.content)
	else:
		print("ERROR IN REQUIRED VOICE SPECIFICATION")