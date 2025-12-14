from langchain_groq import ChatGroq
from dotenv import load_dotenv
from states import Plan
from prompts import genSysPrompt
from langgraph.constants import END
from langgraph.graph import StateGraph

load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-120b")


#planning node of lang graph
def planner_agent(state: dict) -> dict:
    user_prompt = state["user_prompt"]
    plan_resp = llm.with_structured_output(Plan).invoke(genSysPrompt(user_prompt))
    return {'plan':plan_resp}

graph = StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.set_entry_point("planner")

agent = graph.compile()
user_prompt= "create a simple web app for calculator"
result = agent.invoke({"user_prompt":user_prompt})
print(result)