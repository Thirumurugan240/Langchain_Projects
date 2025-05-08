from langchain_groq import ChatGroq

def get_groq_llm():
    return ChatGroq(
        model_name = "llama3-8b-8192",
        groq_api_key="your_api_key",
        temperature=0.5
    )
