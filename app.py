import streamlit as st
from llm import ask_llm

st.set_page_config(page_title="HackSynthesis: Autism Care Assistant 🤖", page_icon="🤖")

st.title("HackSynthesis: Autism Care Assistant 🤖")
st.markdown(
    "Enter your observations about a child’s behavior or symptoms, and the AI will suggest autism care strategies."
)


user_input = st.text_area("Describe the child's behavior or concerns:", height=150)

if st.button("Get AI Suggestions") and user_input.strip():
    with st.spinner("Analyzing..."):
      
        prompt_detection = f"""
You are an expert in child psychology. Based on the following observations, classify the autism level as 'mild', 'moderate', or 'severe', and briefly explain why:

Observations:
{user_input}
"""
        autism_level_response = ask_llm(prompt_detection)

    
        prompt_care = f"""
You are an autism care assistant. The child is classified as: {autism_level_response}.
Provide 3-5 practical, parent-friendly strategies to support the child.
"""
        care_suggestions = ask_llm(prompt_care)

    st.subheader("🧩 Autism Level Detection:")
    st.write(autism_level_response)

    st.subheader("📌 Suggested Care Strategies:")
    st.write(care_suggestions)
