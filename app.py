import streamlit as st
from llm import ask_llm

st.set_page_config(page_title="Mindpal: Autism Care Assistant 🤖", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
    /* Background */
    body {
        background: linear-gradient(135deg, #e3f2fd, #fce4ec);
        font-family: "Arial", sans-serif;
        color: #333333;
    }

    /* Titles */
    h1, h2, h3 {
        color: #2c3e50;
        font-weight: 700;
    }

    /* Markdown text */
    .stMarkdown {
        color: #37474f;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Text area */
    textarea {
        background-color: #ffffff !important;
        border: 2px solid #90caf9 !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        padding: 12px !important;
    }

    /* Button */
    div.stButton > button {
        background: linear-gradient(90deg, #42a5f5, #ec407a);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s ease;
    }
    div.stButton > button:hover {
        background: linear-gradient(90deg, #1e88e5, #d81b60);
        transform: scale(1.05);
    }

    /* Subheaders */
    h2 {
        border-bottom: 2px solid #90caf9;
        padding-bottom: 6px;
        margin-top: 20px;
    }

    /* Result boxes */
    .result-box {
        background: #ffffff;
        border-radius: 12px;
        padding: 15px;
        margin-top: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        border-left: 6px solid #42a5f5;
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

🧩 DISCLAIMER: *Mindpal: Autism Care Assistant* is an educational tool designed to provide general guidance and strategies for learning about autism.  
It is **not** a medical or diagnostic tool. Always seek professional evaluation when in doubt.
"""
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
    st.markdown(f"<div class='result-box'><b>Detected Stage:</b> {autism_level_response}</div>", unsafe_allow_html=True)

    st.subheader("📌 Suggested Care Strategies:")
    st.markdown(f"<div class='result-box'>{care_suggestions}</div>", unsafe_allow_html=True)
