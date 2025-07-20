import os
import google.generativeai as genai
from dotenv import load_dotenv

import os
from dotenv import load_dotenv
import requests

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.0-flash"


def generate_response(prompt: str, user_input: str) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt + "\n\n" + user_input}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        raise Exception(f"Gemini API Error: {response.status_code}, {response.text}")


load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-2.0-flash")
#
#
# def ask_gemini(prompt: str, pdf_text: str) -> dict:
#     response = model.generate_content([prompt, pdf_text])
#     return response.text
