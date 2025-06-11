import os
import streamlit as st
from langchain_community.tools import Tool
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

# Load API keys
groq_api_key = os.getenv("GROQ_API_KEY")
serp_api_key = os.getenv("SERP_API_KEY")

# Initialize Groq model
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="Gemma2-9b-It",  # You can change this to llama3 or gemma
    temperature=0.2
)

# Define SerpAPI Tool
search = SerpAPIWrapper(serpapi_api_key=serp_api_key)
news_tool = Tool(
    name="News Search",
    func=search.run,
    description="Search for recent news and current events using SerpAPI"
)

# Chain of Thought logic in the prompt with concise answer
def chain_of_thought_prompt(query):
    return f"""
You are an AI assistant that thinks step by step before using tools.
Use this format:
Thought: Describe your thinking
Action: News Search
Action Input: "<your search query>"

Only use the tool if necessary, otherwise finish with:
Final Answer: Provide a brief and concise summary in response to the question, and answer should be longer than 8 sentence  .

Now answer the following:
Question: {query}
"""

# Initialize the agent with SELF_ASK_WITH_SEARCH
agent = initialize_agent(
    tools=[news_tool],
    llm=llm,
    agent_type=AgentType.SELF_ASK_WITH_SEARCH,  # Use SELF_ASK_WITH_SEARCH agent
    handle_parsing_errors=True,
    verbose=True
)

# Streamlit UI setup
st.set_page_config(page_title="Groq News Chatbot", page_icon="🧠")
st.title("🧠 Groq-Powered News Chatbot")
st.markdown("Ask anything! It can search recent news and reason step-by-step using Groq LLM.")

# Input from user
user_input = st.text_input("Enter your question:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            # Step 1: Use Chain of Thought prompt
            thought_prompt = chain_of_thought_prompt(user_input)

            # Step 2: Get detailed response (includes reasoning and tool decision)
            detailed_response = agent.run(thought_prompt)

            # Step 3: Display intermediate steps (chain of thought)
            st.subheader("Chain of Thought:")
            st.write(detailed_response)

            # Final answer output
            st.success("Here's the full response with reasoning and final answer:")
            st.write(detailed_response)
             # Display only the final answer part

        except Exception as e:
            st.error(f"Something went wrong: {e}")
