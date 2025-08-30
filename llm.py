from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os

model_name = "mistralai/Mistral-7B-Instruct-v0.2"


tokenizer = AutoTokenizer.from_pretrained(model_name, token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
model = AutoModelForCausalLM.from_pretrained(model_name, token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

def ask_llm(prompt):
    response = pipe(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    return response[0]["generated_text"]
