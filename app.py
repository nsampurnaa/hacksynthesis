import streamlit as st
from kb import autism_care
from llm import ask_llm

st.title("HackSynthesis: Autism Care Assistant 🤖")

level = st.selectbox("Select autism care level:", ["mild", "moderate", "severe"])
st.write("📌 Suggested strategies:")
for tip in autism_care[level]:
    st.write(f"- {tip}")

user_input = st.text_area("💬 Ask the AI for additional suggestions:")

if st.button("Get AI Help"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = ask_llm(user_input)
        st.success("AI Suggestion:")
        st.write(response)
    else:
        st.warning("Please enter a question before asking.")
