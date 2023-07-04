from os import environ
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = environ.get("GPTKEY")

# Deleuze
system_prompt = "Je souhaite que nous discutions. Tu dois incarner Gilles Deleuze. Tu répondras toujours dans le style de Deleuze. Tu citeras directement Deleuze dès que possible, a la première personne. Tu commenceras toutes tes phrases par une question et termineras par une question. Ta première phrase sera 'Bonjour, je suis le fantôme de Gilles Deleuze, comment puis-je vous renseigner ?'"


# Joey Starr
# system_prompt = "Je souhaite que nous discutions. Tu dois incarner Joey Starr. Tu répondras toujours dans le style de Joey Starr. Tu citeras directement les paroles du groupe de musique NTM dès que possible, a la première personne. Ta première phrase sera 'Mec, moi c'est Joey Starr, le king du rap. J’suis marqué au fer c’est comme si je touchais plus terre'"
messages = [{"role": "system", "content": system_prompt}]

while True:
    try:
        inputs = input()
        if inputs:
            print("Me: ", inputs)
            messages.append({"role": "user", "content": inputs})
        print("Please wait...")
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        response = completion['choices'][0]['message']['content']
        print("StarrGPT: ", response)
        messages.append({"role": "assistant", "content": response})
    except (InterruptedError, KeyboardInterrupt):
        break
