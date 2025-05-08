import streamlit as st
from ollama_config import query_ollama

st.set_page_config(page_icon='Local GenAI Assistant')

st.title('Gen AI Assistant (Powered by ollama)')

prompt = st.text_area('Ask me everything:', height=150)

if st.button('Generate'):
    with st.spinner('Thinking..'):
        response = query_ollama(prompt)
        st.markdown('### Response:')
        st.write(response)