from tools import tool_executor
from langgraph.prebuilt import ToolInvocation

from langchain_core.agents import AgentActionMessageLog
def execute_tools(state):

    messages = [state['agent_outcome'] ]
    last_message = messages[-1]
    ######### human in the loop ###########   
    # human input y/n 
    # Get the most recent agent_outcome - this is the key added in the `agent` above
    # state_action = state['agent_outcome']
    # human_key = input(f"[y/n] continue with: {state_action}?")
    # if human_key == "n":
    #     raise ValueError
    
    tool_name = last_message.tool
    arguments = last_message
    if tool_name == "Search" or tool_name == "Sort" or tool_name == "Toggle_Case":
        
        if "return_direct" in arguments:
            del arguments["return_direct"]
    action = ToolInvocation(
        tool=tool_name,
        tool_input= last_message.tool_input,
    )
    response = tool_executor.invoke(action)
    return {"intermediate_steps": [(state['agent_outcome'],response)]}

def should_continue(state):

            messages = [state['agent_outcome'] ] 
            last_message = messages[-1]
            if "Action" not in last_message.log:
                return "end"
            else:
                arguments = state["return_direct"]
                if arguments is True:
                    return "final"
                else:
                    return "continue"
                
def first_agent(inputs):
            action = AgentActionMessageLog(
            tool="Search",
            tool_input=inputs["input"],
            log="",
            message_log=[]
            )
            return {"agent_outcome": action}