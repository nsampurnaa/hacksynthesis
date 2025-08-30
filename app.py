import streamlit as st
from llm import ask_llm

st.set_page_config(page_title="MindPal: Autism Care Chatbot 🤖", page_icon="🤖")
st.title("MindPal: Autism Care Chatbot 🤖")
st.markdown("The AI will ask questions about your child and suggest care strategies based on the conversation.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "conversation_active" not in st.session_state:
    st.session_state.conversation_active = True
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def get_ai_prompt(chat_history):
    conversation_text = ""
    for msg in chat_history:
        conversation_text += f"{msg['role'].capitalize()}: {msg['content']}\n"
    prompt = f"""
You are an expert autism care assistant. You are talking to a parent to determine if their child has autism.
Ask questions step by step, wait for the user's response, and gradually assess autism severity (mild, moderate, severe).
After enough information, give a conclusion and 3-5 practical strategies. 

Conversation so far:
{conversation_text}
AI:
"""
    return prompt

chat_container = st.container()
with chat_container:
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**AI:** {msg['content']}")

if st.session_state.conversation_active:
    st.session_state.user_input = st.text_input("Your response:", value=st.session_state.user_input, key="input_box")
    if st.button("Send") and st.session_state.user_input.strip():
        user_msg = st.session_state.user_input.strip()
        st.session_state.chat_history.append({"role": "user", "content": user_msg})
        st.session_state.user_input = ""
        prompt = get_ai_prompt(st.session_state.chat_history)
        ai_response = ask_llm(prompt)
        st.session_state.chat_history.append({"role": "ai", "content": ai_response})
