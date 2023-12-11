from app import get_sql

import streamlit as st

st.title("North America Countries Database")

question = st.text_input("Question: ")
if question:
    chain = get_sql()
    ans = chain.run(question)
    st.header('Answer: ')
    st.write(ans)
