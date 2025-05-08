import streamlit as st
from langchain_core.messages import HumanMessage
from graph_bot import build_graph, init_state

st.set_page_config(page_title="LangGraph Chatbot")
st.title("🤖 LangGraph + Groq Chatbot")

if "state" not in st.session_state:
    st.session_state.graph = build_graph()
    st.session_state.state = init_state()
    st.session_state.chat_history = []

user_input = st.chat_input("Ask something...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.state["messages"].append(HumanMessage(content=user_input))

    result = st.session_state.graph.invoke(st.session_state.state)
    ai_msg = result["messages"][-1]

    st.chat_message("ai").write(ai_msg.content)
    st.session_state.state = result
