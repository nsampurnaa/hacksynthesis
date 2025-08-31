import streamlit as st
from llm import ask_llm


st.set_page_config(
    page_title="Mindpal: Autism Care Assistant 🤖",
    page_icon="🤖",
    layout="centered"
)


st.markdown("""
    <style>
    body {
        background: linear-gradient(120deg, #fcefee, #e8faff);
        font-family: 'Trebuchet MS', sans-serif;
    }
    .big-title {
        font-size: 2.2em;
        color: #5a189a;
        text-align: center;
        font-weight: bold;
    }
    .subtitle {
        font-size: 1.1em;
        color: #333;
        text-align: center;
        margin-bottom: 20px;
    }
    .disclaimer {
        background: #fff3cd;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #ffeeba;
        color: #856404;
        font-size: 0.9em;
        margin-top: 15px;
    }
    .card {
        background: white;
        padding: 18px;
        border-radius: 16px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<div class='big-title'>Mindpal: Autism Care Assistant 🤖</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your friendly AI companion for learning autism care 💜</div>", unsafe_allow_html=True)


st.markdown(
    """
**Autism Levels:**  
- 🟢 **Mild:** Minor difficulties, may need minimal support.  
- 🟡 **Moderate:** Noticeable difficulties, may need structured support.  
- 🔴 **Severe:** Significant difficulties, needs intensive support.  
"""
)

st.markdown(
    """
**Please describe things like:**  
✨ Social interactions (eye contact, responding to name)  
✨ Communication (speech, gestures, tone)  
✨ Repetitive behaviors (hand flapping, rocking)  
✨ Interests and play style  
✨ Reactions to changes or sensory input  
✨ Any other unusual behavior you noticed  
"""
)

# ⚠️ Disclaimer
st.markdown(
    """
    <div class='disclaimer'>
    🧩 <b>Disclaimer:</b> Mindpal is an <b>educational tool</b> designed to provide 
    general guidance and strategies for learning about autism.  
    It is <b>not</b> a medical or diagnostic tool.  
    Please consult professionals for evaluation, diagnosis, or treatment.
    </div>
    """, unsafe_allow_html=True
)


user_input = st.text_area("💬 Describe the child's behavior or concerns:", height=200)

if st.button("✨ Get AI Suggestions ✨") and user_input.strip():
    with st.spinner("🔍 Analyzing behavior... please wait"):
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

  
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("🧩 Autism Level Detection (3 Stages)")
    st.markdown(f"**Detected Stage:** {autism_level_response}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📌 Suggested Care Strategies")
    st.write(care_suggestions)
    st.markdown("</div>", unsafe_allow_html=True)
