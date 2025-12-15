from logging import config
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from states import Plan, TaskPlan, CoderState
from prompts import genSysPrompt, architect_prompt, coder_prompt
from langgraph.constants import END
from langgraph.graph import StateGraph
from langchain_core.globals import set_verbose, set_debug
from tools import *
from langchain.agents import create_agent


load_dotenv()

set_debug(True)
set_verbose(True)
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

def coder_agent(state: dict) -> dict:
    coder_state:CoderState = state.get('coder_state')
    if coder_state is None:
        coder_state = CoderState(task_plan=state['task_plan'], current_step_index=0)
    
    
    implementation_steps = coder_state.task_plan.implementation_steps
    
    if coder_state.current_step_index >= len(implementation_steps):
        return {"coder_state": coder_state, "status":"Done"}
    
    coder_tools=[read_file,write_file,list_files,get_current_directory]
    
    current_task = implementation_steps[coder_state.current_step_index]
    
    
    current_path = current_task.filepath
    current_description = current_task.task_description
    existing_content = read_file.run(current_path)
   
    user_prompt = f"Task:{current_description} , Filepath:{current_path}, Existing file content:{existing_content}, Use write_file(path,content) to save your changes."
    
    sys_prompt = coder_prompt()
    #current_resp = llm.invoke(sys_prompt + user_prompt)
    react_agent = create_agent(llm,coder_tools)
    current_resp = react_agent.invoke({"messages":[
        {'role':'system','content':sys_prompt},
        {'role':'user','content':user_prompt}
    ]})
    coder_state.current_step_index += 1
    return {"coder_state": coder_state}
    
    
    
    
graph = StateGraph(dict)
graph.add_node("planner",planner_agent)
graph.add_node("architect",architect_agent)
graph.add_node("coder",coder_agent)
graph.add_edge(start_key="planner",end_key="architect")
graph.add_edge(start_key="architect",end_key="coder")
graph.add_conditional_edges(
    "coder",
    lambda s: "END" if s.get("status") == "Done" else "coder",
    {"END": END, "coder": "coder"}
)
graph.set_entry_point("planner")

agent = graph.compile()

if __name__ == "__main__":
    user_prompt= "create a simple web app for calculator"
    result = agent.invoke({"user_prompt":user_prompt},config={"recursion_limit":100})
    print("Result:", result)


