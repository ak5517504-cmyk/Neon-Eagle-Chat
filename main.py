import streamlit as st
from google import genai

st.title("Neon Eagle Chat")

api_key = st.text_input("Enter Gemini API Key", type="password")

if api_key:
    # Nayi library ka client initialization
    client = genai.Client(api_key=api_key)

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
            try:
                # Nayi library ke hisab se model call
                response = client.models.generate_content(
                    model='gemini-1.5-flash',
                    contents=prompt
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error: {e}")
