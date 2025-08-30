from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

def ask_llm(prompt):
    out = llm_pipeline(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
    return out[0]["generated_text"]
