import os
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools

import wikipedia
from dotenv import load_dotenv
from openkey import openai_api_key
import json


from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
memory= ConversationBufferMemory()
llm= ChatOpenAI()
tools = load_tools([ 'wikipedia',
'llm-math',
#'google-search',
'python_repl',
#'wolfram-alpha'
'terminal',
#'news-api'
#'podcast-apt',
#'openweathermap-api'
], llm=llm)
agent =initialize_agent(
tools, llm,
agent= AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
verbose=True,
memory=memory
)
agent.run("What's up ChatGPT?")