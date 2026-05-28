import streamlit as st
import google.generativeai as genai

st.title("Neon Eagle Chat")
api_key = st.text_input("Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel('gemini-pro')
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
      
