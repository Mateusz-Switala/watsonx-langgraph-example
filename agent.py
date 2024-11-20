import os
from pathlib import Path

from langchain_ibm import ChatWatsonx
from langchain_community.tools.tavily_search import TavilySearchResults

from dotenv import load_dotenv

load_dotenv()

from langgraph.prebuilt import create_react_agent

chat_model = ChatWatsonx(model_id="meta-llama/llama-3-1-70b-instruct",
                         project_id=os.environ.get('WX_PROJECT_ID'))

tools = [TavilySearchResults(max_results=2)]

graph = create_react_agent(chat_model, tools)


