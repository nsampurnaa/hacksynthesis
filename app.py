import streamlit as st
import numpy as np
from hrv import fake_hrv_analysis
from kb import autism_care
from llm import ask_llm

st.set_page_config(
    page_title="MindPal",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

st.title("🧠 MindPal — Autism Detection & Support Demo")
st.write("Enter ECG values (comma-separated) to simulate detection and get activity suggestions.")

ecg_input = st.text_area("", "0.1,0.2,0.3,0.5", height=100)

if st.button("Analyze"):
    try:
        ecg_values = np.array([float(x) for x in ecg_input.split(",")])
        severity = fake_hrv_analysis(ecg_values)
        st.subheader(f"Predicted Autism Spectrum: {severity.capitalize()}")
        suggestions = autism_care[severity]

        st.write("**Knowledge Base Suggestions:**")
        for s in suggestions:
            st.markdown(f"- {s}")

        prompt = f"The child is showing {severity} autism traits. Suggest two simple activities parents can do at home."
        llm_response = ask_llm(prompt)

        st.subheader("AI Suggested Activities")
        st.write(llm_response)

    except Exception as e:
        st.error(f"Error: {e}")
