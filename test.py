import requests

url = "https://realistic-text-to-speech.p.rapidapi.com/v3/get_all_v2_voices"

headers = {
	"X-RapidAPI-Key": "f6b9f7e5a3mshc27a2083997f30fp1d3f5djsnd9b63dcb026b",
	"X-RapidAPI-Host": "realistic-text-to-speech.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())