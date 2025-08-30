import os
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

def ask_llm(prompt: str) -> str:
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    return data[0]["generated_text"]
