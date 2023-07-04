import requests
from os import environ
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": f"Bearer {apikey}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

history = {
    "past_user_inputs": [],
    "generated_responses": []
}

while True:
    try:
        question = input("\nAsk me something:\n")
        inputs = {
            "past_user_inputs": history.get("past_user_inputs"),
            "generated_responses": history.get("generated_responses"),
            "text": question
        }
        output = query(inputs)

        error = output.get("error")
        generated_text = output.get("generated_text")
        if error:
            print("Error:", error)
        else:
            print(generated_text)
        
        history.get("past_user_inputs").append(question)
        history.get("generated_responses").append(generated_text)
    except KeyboardInterrupt:
        print("Bye!")
        break


# output = query({
# 	"inputs": {
# 		"past_user_inputs": ["Which movie is the best ?"],
# 		"generated_responses": ["It's Die Hard for sure."],
# 		"text": "Can you explain why ?"
# 	},
# })
# print(output.get("generated_text"))