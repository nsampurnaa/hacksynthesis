import streamlit as st
from llm import ask_llm

st.set_page_config(page_title="Mindpal: Autism Care Assistant 🤖", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff, #cfe0fc, #fef6ff);
    }

    /* Title */
    h1 {
        text-align: center;
        font-family: "Trebuchet MS", sans-serif;
        color: #2a3d66;
    }

    /* Subheaders */
    h2, h3 {
        color: #30475e;
        font-family: "Verdana", sans-serif;
    }

    /* Regular text */
    p, li {
        font-size: 16px;
        color: #222831;
    }

    /* Text area */
    textarea {
        border-radius: 12px !important;
        border: 2px solid #6c63ff !important;
        background-color: #f9f9ff !important;
        color: #222831 !important;
    }

    /* Button */
    div.stButton > button {
        background: linear-gradient(90deg, #6c63ff, #4facfe);
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #4facfe, #6c63ff);
        transform: scale(1.05);
    }

    /* Disclaimer */
    .disclaimer {
        font-size: 14px;
        color: #d90429;
        font-style: italic;
        padding: 12px;
        border-left: 4px solid #d90429;
        background: #fff5f5;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Mindpal: Autism Care Assistant 🤖")
st.markdown(
    "Enter your observations about a child’s behavior or symptoms, and the AI will suggest autism care strategies."
)

st.markdown(
    """
**Autism Levels:**  
- **Mild:** Minor difficulties with social interactions or communication, may need minimal support.  
- **Moderate:** Noticeable difficulties in communication and behavior, may require structured support.  
- **Severe:** Significant difficulties, requires intensive support and interventions.  
"""
)

st.markdown(
    """
**Please describe things like:**  
- Social interactions (eye contact, responding to name)  
- Communication (speech, gestures, tone)  
- Repetitive behaviors (hand flapping, rocking)  
- Interests and play style  
- Reactions to changes or sensory input  
- Any other unusual behavior you noticed  
"""
)

st.markdown(
    """
<div class="disclaimer">
🧩 DISCLAIMER: Mindpal: Autism Care Assistant is an educational tool designed to provide general guidance and strategies for learning about autism.  
It is not a medical or diagnostic tool. The observations and suggestions are intended for educational purposes only and should not replace professional evaluation, diagnosis, or treatment.
</div>
""",
    unsafe_allow_html=True,
)

user_input = st.text_area("Describe the child's behavior or concerns:", height=200)

if st.button("Get AI Suggestions") and user_input.strip():
    with st.spinner("Analyzing..."):
        prompt_detection = f"""
You are an expert in child psychology. Based on the following observations, classify the autism level into one of three stages: 'Mild', 'Moderate', or 'Severe'. Briefly explain why and reference the stage definitions:

Observations:
{user_input}
"""
        autism_level_response = ask_llm(prompt_detection)

        prompt_care = f"""
You are an autism care assistant. The child is classified as: {autism_level_response}.
Provide 3-5 practical, parent-friendly strategies to support the child.
"""
        care_suggestions = ask_llm(prompt_care)

    st.subheader("🧩 Autism Level Detection (3 Stages):")
    st.markdown(f"**Detected Stage:** {autism_level_response}")

    st.subheader("📌 Suggested Care Strategies:")
    st.write(care_suggestions)
