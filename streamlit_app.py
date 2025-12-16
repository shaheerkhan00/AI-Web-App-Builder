import streamlit as st
from agent.graph import agent

def main():
    st.title("App Builder - AI Agent (Loveable Clone)")
    recursion_limit = st.slider(
        "Recursion Limit",
        min_value = 10,
        max_value = 1000,
        help="Recursion Limit",
    )
    user_prompt = st.text_area("Enter your prompt",placeholder="Describe your project",height=200)
    if st.button("Run",type="primary"):
        if user_prompt:
            try:
                result = agent.invoke(
                    {"user_prompt": user_prompt},
                    {"recursion_limit": recursion_limit}
                )
                st.subheader("Project :")
                st.write(result)
            except Exception as e:
                st.error(e)
        else:
            st.warning("Please enter a project prompt!")




if __name__ == "__main__":
    # Note: No need to call main() directly in Streamlit
    # Streamlit automatically runs the script
    main()
    pass