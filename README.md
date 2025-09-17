# Groq-Powered News Chatbot

This project is an AI-driven chatbot application that combines the reasoning power of Groq's LLM (e.g., Gemma2-9b-It) with real-time data fetching from SerpAPI (Google Search API). The chatbot is built with Streamlit, providing a user-friendly web interface for interacting with the AI.

## Features

*   **Real-time News Search:** Utilizes SerpAPI to fetch the latest news and information from the web.
*   **Conversational AI:** Leverages Groq's powerful language models for natural and context-aware conversations.
*   **Chain of Thought Reasoning:** The agent is designed to think step-by-step, providing a transparent reasoning process for its answers.
*   **Simple UI:** A clean and simple user interface built with Streamlit.

## How it works

The application uses a combination of LangChain and Streamlit to create the chatbot. Here's a breakdown of the architecture:

1.  **Streamlit UI:** The user interacts with the chatbot through a simple web interface built with Streamlit.
2.  **LangChain Agent:** A LangChain agent is initialized with a Groq language model and a SerpAPI tool.
3.  **Groq LLM:** The Groq language model (`Gemma2-9b-It`) is used for its fast inference speed and reasoning capabilities.
4.  **SerpAPI Tool:** The SerpAPI tool allows the agent to search for recent news and current events.
5.  **Chain of Thought Prompt:** A custom prompt is used to guide the agent's reasoning process, encouraging it to think step-by-step before providing an answer.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/RohitBind123/News_Agent_ChatBot.git
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your environment variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```
    GROQ_API_KEY="your_groq_api_key"
    SERP_API_KEY="your_serp_api_key"
    ```

## Usage

1.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
2.  **Open your browser:**
    The app will open in your browser at `http://localhost:8501`.
3.  **Ask a question:**
    Type your question in the input box and press Enter. The chatbot will provide a detailed answer with its reasoning process.

## Technologies Used

*   **Streamlit:** For the web interface.
*   **LangChain:** For the agent and tool integration.
*   **Groq:** For the language model.
*   **SerpAPI:** For real-time news search.
*   **Python-dotenv:** For managing environment variables.