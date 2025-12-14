
def genSysPrompt(user_prompt):
     system_planning_prompt = f"""
           You are the PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan
            User_request :{user_prompt}"""
     return system_planning_prompt





