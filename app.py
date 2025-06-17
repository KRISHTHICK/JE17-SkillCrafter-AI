import streamlit as st
from rag_engine import get_learning_card
from micro_agent import ask_micro_agent

st.set_page_config(page_title="🧠 SkillCrafter AI", layout="wide")
st.title("🧪 SkillCrafter AI – Build Micro Skills Fast")

st.markdown("Upload a learning document and ask the agent for lessons or flashcards.")

uploaded_file = st.file_uploader("📄 Upload PDF or text document", type=["pdf", "txt"])

query = st.text_input("🔍 What micro-skill or topic do you want to learn?")

if uploaded_file and query:
    st.subheader("📚 Learning Card")
    st.markdown(get_learning_card(uploaded_file, query))

    st.subheader("🤖 Ask Micro-Learning Agent")
    user_q = st.text_input("Ask anything related to this skill:")
    if user_q:
        response = ask_micro_agent(user_q)
        st.markdown(response)
