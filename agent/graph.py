from langchain_groq import ChatGroq
from dotenv import load_dotenv
from states import Plan
from prompts import genSysPrompt


load_dotenv()
llm = ChatGroq(model="openai/gpt-oss-120b")

user_prompt= "create a simple web app for calculator"
#planning node of lang graph

system_planning_prompt = genSysPrompt(user_prompt)
plan_resp = llm.with_structured_output(Plan).invoke(system_planning_prompt)

#resp = llm.with_structured_output(Schema).invoke(
 #   "Extract price and EPS from this: Toyota's new model is priced at $53,000. The company reported EPS of $8.50 for Q4."
#)

print(plan_resp)