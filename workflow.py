



from langgraph.graph import END, START,StateGraph


from state import AgentState


from agent import chatbot
workflow = StateGraph(AgentState)
workflow.add_node("chatbot",chatbot)
workflow.add_edge(START,"chatbot")
workflow.add_edge("chatbot",END)
app=workflow.compile()