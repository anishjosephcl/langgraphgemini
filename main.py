from langchain import hub
from langchain.agents import Tool, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (
   
    HumanMessage,
)
import os
from typing import TypedDict, Annotated, Union
from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.messages import BaseMessage
import operator
from typing import TypedDict, Annotated
from langchain_core.agents import AgentFinish
from langgraph.prebuilt.tool_executor import ToolExecutor
from langgraph.prebuilt import ToolInvocation
from langgraph.graph import END, StateGraph
from langchain_core.agents import AgentActionMessageLog
import streamlit as st
from workflow import app
st.set_page_config(page_title="LangChain Agent", layout="wide")


    # Streamlit UI elements
st.title("LangGraph Agent + Gemini Pro + Custom Tool + Streamlit")

    # Input from user
input_text = st.text_area("Enter your text:")
    
if st.button("Run Agent"):
      
    user_input = {"messages": [input_text]}
    for event in app.stream(user_input):
        st.write(event.values())
    
   