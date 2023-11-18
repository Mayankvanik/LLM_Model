from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.llms import GooglePalm


api_key = 'AIzaSyAgeKZthVRtjrFNan4NFOvQdS_tjPbcv3k'
llm1 = GooglePalm(google_api_key=api_key,temperature=0.2)

def get_sql():
    db_user = "root"
    db_password = "Mayankbiker44+"
    db_host = "localhost"
    db_name = "north_america"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
    toolkit = SQLDatabaseToolkit(db=db, llm=llm1)
    agent_executor = create_sql_agent(
        llm=llm1,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,)

    return agent_executor

if __name__ == "__main__":
    agent_executor = get_sql()
    print(agent_executor.run('land area of usa'))

