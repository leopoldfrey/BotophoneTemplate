import requests
from os import environ
from dotenv import load_dotenv

load_dotenv()

apikey = environ.get("GPTKEY")
API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom-560m"
headers = {"Authorization": f"Bearer {apikey}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I am King Charles III and a think AI is ",
})
print(output)