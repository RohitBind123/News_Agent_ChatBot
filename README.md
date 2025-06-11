# News_Agent_ChatBot
This is an intelligent chatbot powered by Groq LLM and SerpAPI, built using LangChain and Streamlit. It can answer user queries by performing step-by-step reasoning and fetching real-time news data using Google Search.

🚀 Features
💡 Uses Groq's Gemma2-9b-It model (or switchable to LLaMA3)

🌐 Integrates with SerpAPI to fetch recent and relevant news

🧠 Uses Chain-of-Thought reasoning for better decision-making

💬 Streamlit web UI for real-time interaction

🔍 AgentType: SELF_ASK_WITH_SEARCH for smart tool use

📁 Project Structure
├── .env                   # Environment variables (API keys)
├── app.py                 # Main Streamlit app script
├── README.md              # Project documentation

🔑 Prerequisites
You need the following API keys:

GROQ_API_KEY – for accessing Groq's LLM

SERP_API_KEY – for querying news via SerpAPI

Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key_here
SERP_API_KEY=your_serpapi_key_here

🧪 Installation
Install dependencies:
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py

🧠 How it Works
The user enters a question.

The app generates a chain-of-thought prompt with step-by-step reasoning.

If required, it triggers SerpAPI to fetch real-time news.

The LangChain agent uses the Groq LLM to decide the final answer.

Displays both the reasoning chain and the final summarized answer.

