
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


def coder_prompt()-> str:
      CODER_PROMPT = """
           You are the CODER agent.
          You are implementing a specific engineering task.
             You have access to EXACTLY these tools (use these names EXACTLY as shown):
             
             AVAILABLE TOOLS:
             - read_file(path: str) -> str
             - write_file(path: str, content: str) -> str  
             - list_files(directory: str) -> str
             - get_current_directory() -> str
             
             DO NOT invent or use any other tool names like 'repo_browser.list_files' or similar.
             ONLY use the 4 tools listed above with their EXACT names.

           Always:
           - Review all existing files to maintain compatibility.
         - Implement the FULL file content, integrating with other modules.
           - Maintain consistent naming of variables, functions, and imports.
          - When a module is imported from another file, ensure it exists and is implemented as described.
            """
      return CODER_PROMPT