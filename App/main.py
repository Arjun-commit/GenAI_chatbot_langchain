# Import necessary modules and setup for FastAPI, LangGraph, and LangChain
from fastapi import FastAPI, Request   # FastAPI framework for creating the web application
from pydantic import BaseModel  # BaseModel for structured data data models
from typing import List  # List type hint for type annotations
from langchain_community.tools.tavily_search import TavilySearchResults  # TavilySearchResults tool for handling search results from Tavily
import os  # os module for environment variable handling
from langgraph.prebuilt import create_react_agent  # Function to create a ReAct agent
from langchain_groq import ChatGroq  # ChatGroq class for interacting with LLMs

from fastapi.templating import Jinja2Templates  # Jinja2 for templates
from pathlib import Path  # To resolve the template path
from fastapi.staticfiles import StaticFiles


# Retrieve and set API keys for external tools and services
groq_api_key = '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'  # Groq API key
os.environ["TAVILY_API_KEY"] = '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'  # Set Tavily API key

# Predefined list of supported model names
MODEL_NAMES = [
    "llama3-70b-8192",  # Model 1: Llama 3 with specific configuration
    "mixtral-8x7b-32768"  # Model 2: Mixtral with specific configuration
]

# Initialize the TavilySearchResults tool with a specified maximum number of results.
tool_tavily = TavilySearchResults(max_results=2)  # Allows retrieving up to 2 results


# Combine the TavilySearchResults and ExecPython tools into a list.
tools = [tool_tavily, ]

# FastAPI application setup with a title
app = FastAPI(title='LangGraph AI Agent')

# Define the request schema using Pydantic's BaseModel
class RequestState(BaseModel):
    model_name: str  # Name of the model to use for processing the request
    system_prompt: str  # System prompt for initializing the model
    messages: List[str]  # List of messages in the chat

# Define an endpoint for handling chat requests
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to interact with the chatbot using LangGraph and tools.
    Dynamically selects the model specified in the request.
    """
    if request.model_name not in MODEL_NAMES:
        # Return an error response if the model name is invalid
        return {"error": "Invalid model name. Please select a valid model."}

    # Initialize the LLM with the selected model
    llm = ChatGroq(groq_api_key=groq_api_key, model_name=request.model_name)

    # Create a ReAct agent using the selected LLM and tools
    agent = create_react_agent(llm, tools=tools, state_modifier=request.system_prompt)

    # Create the initial state for processing
    state = {"messages": request.messages}

    # Process the state using the agent
    result = agent.invoke(state)  # Invoke the agent (can be async or sync based on implementation)

    # Return the result as the response
    return result

app.mount("/static", StaticFiles(directory="App/static"), name="static")

templates = Jinja2Templates(directory="App/templates")

# Define route to serve the UI (index.html)
@app.get("/ui")
def get_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Run the application if executed as the main script
if __name__ == '__main__':
    import uvicorn  # Import Uvicorn server for running the FastAPI app
    uvicorn.run(app, host='127.0.0.1', port=8000)  # Start the app on localhost with port 8000