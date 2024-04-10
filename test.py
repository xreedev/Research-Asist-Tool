import requests
from api import texttospeech_apikey as api

url = "https://realistic-text-to-speech.p.rapidapi.com/v3/get_all_v2_voices"

headers = {
	"X-RapidAPI-Key": api,
	"X-RapidAPI-Host": "realistic-text-to-speech.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())