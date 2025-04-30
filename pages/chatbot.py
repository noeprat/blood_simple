import streamlit as st
import pandas as pd
from streamlit import session_state as ss
from utils.chatbot_agent import Chatbot



import streamlit as st

st.set_page_config(page_title="Chatbot")

st.title("Enhanced GPT Clone for Medical Assistance Chatbot")

client = Chatbot()

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F3CFC6;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)




if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("I am a medical assistant. How can I help you ?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.ask(prompt)
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
