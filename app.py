import streamlit as st
from query_llm import query_llm

st.title("📊 ITC Financial Analyzer (2023–2024)")
query = st.text_input("Ask a question (e.g., ITC revenue in 2024):")

if query:
    with st.spinner("Thinking..."):
        answer, page = query_llm(query)
    st.success(answer)
    st.caption(f"📚 Source: Annual Report, Page {page}")