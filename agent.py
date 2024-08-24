from llm import llm
from state import AgentState
def chatbot(state:AgentState):
  return {"messages":llm.invoke(state['messages'])}