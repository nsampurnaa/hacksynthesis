import os
import requests
API_URL = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
    "Content-Type": "application/json"
}

def ask_llm(prompt: str) -> str:
    try:
        payload = {
            "model": "mistralai/mistral-7b-instruct:free",
            "messages": [
                {"role": "system", "content": "You are an assistant that helps parents with autism care strategies."},
                {"role": "user", "content": prompt}
            ]
        }

        resp = requests.post(API_URL, headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()

        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

