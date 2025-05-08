import streamlit as st
import tempfile
from utils.rag_chain import load_docs, create_vectorstore, get_rag_chain

st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title(" RAG Chatbot using LangChain + GROQ")

# Upload section
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    with st.spinner("Processing and indexing the document..."):
        documents = load_docs(temp_file_path)
        vectorstore = create_vectorstore(documents)
        rag_chain = get_rag_chain(vectorstore)

    st.success("Document indexed. Ask your question!")

    user_question = st.text_input("Ask something about your PDF:")

    if user_question:
        with st.spinner(" Generating response..."):
            response = rag_chain({"query": user_question})
            answer = response["result"]
            sources = response["source_documents"]

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Source Chunks"):
            for i, doc in enumerate(sources):
                st.markdown(f"**Source {i+1}**")
                st.write(doc.page_content[:500] + "...")
else:
    st.info("📥 Please upload a PDF to begin.")
