
def genSysPrompt(user_prompt):
     system_planning_prompt = f"""
           You are the PLANNER agent. Convert the user prompt into a COMPLETE engineering project plan
            User_request :{user_prompt}"""
     return system_planning_prompt


def architect_prompt(plan:str)->str:
      ARCHITECT_PROMPT = f"""
      You are the ARCHITECT agent. Given the following project plan, break it down into a DETAILED architecture with components, modules, and their interactions.
      RULES:
      - For each file in the plan, create one or more IMPLEMENTATION TASKS.
      -In each task description:
            * Specify exactly what has to be implemented.
            * Name the variables, functions, classes and components to be defined
            * Mention how this task depends on or will be used by previous tasks
            * Include integration details : imports, expected function signatures, data flow.
      - Ensure that the tasks are ordered logically for implementation.
      - Each step should be SELF-CONTAINED but also carry FORWARD the context from previous steps.
            
      
      Project Plan: {plan}
      
      """
      return ARCHITECT_PROMPT


