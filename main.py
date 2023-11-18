# from langchain.agents import create_sql_agent
# from langchain.agents.agent_types import AgentType
# from langchain.sql_database import SQLDatabase
# from langchain.agents.agent_toolkits import SQLDatabaseToolkit
#from langchain.llms import GooglePalmmain
from app import get_sql

import streamlit as st

st.title("North America Countries Database")

question = st.text_input("Question: ")
if question:
    chain = get_sql()
    ans = chain.run(question)
    st.header('Answer: ')
    st.write(ans)