from huggingface_hub import InferenceClient
import os

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

def ask_llm(prompt: str) -> str:
    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7
        )
        return response
    except Exception as e:
        return f"Error: {str(e)}"
