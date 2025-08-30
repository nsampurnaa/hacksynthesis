import os
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

def ask_llm(prompt: str) -> str:
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()  # raise error if status != 200
        data = response.json()

        # Sometimes HF returns an error in JSON format
        if isinstance(data, dict) and "error" in data:
            return f"⚠️ API Error: {data['error']}"
        
        return data[0]["generated_text"]

    except requests.exceptions.RequestException as e:
        return f"⚠️ Request failed: {str(e)}"
    except ValueError:
        # JSON decode failed
        return f"⚠️ Failed to parse response: {response.text[:200]}"
