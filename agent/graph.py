from langchain_groq import ChatGroq
from dotenv import load_dotenv
from states import Plan, TaskPlan
from prompts import genSysPrompt, architect_prompt
from langgraph.constants import END
from langgraph.graph import StateGraph

load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-120b")


#planning node of lang graph
def planner_agent(state: dict) -> dict:
    user_prompt = state["user_prompt"]
    plan_resp = llm.with_structured_output(Plan).invoke(genSysPrompt(user_prompt))
    if plan_resp is None:
        raise ValueError("Planner agent returned None")
    
    return {'plan':plan_resp}
def architect_agent(state: dict) -> dict:
    plan = state['plan']
    architect_resp = llm.with_structured_output(TaskPlan).invoke(architect_prompt(plan))
    if architect_resp is None:
        raise ValueError("Architect agent returned None")
    architect_resp.plan = plan
    return {"task_plan":architect_resp}

graph = StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_edge(start_key="planner",end_key="architect")
graph.set_entry_point("planner")

agent = graph.compile()

if __name__ == "__main__":
    user_prompt= "create a simple web app for calculator"
    result = agent.invoke({"user_prompt":user_prompt})
    print("Result:", result)


