from langchain.agents import Tool, create_react_agent
from langgraph.prebuilt.tool_executor import ToolExecutor
import os
from langchain_community.tools.tavily_search import TavilySearchResults

os.environ["TAVILY_API_KEY"] = "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"

tavily_tool = TavilySearchResults(max_results=5)
    
tools = [
      Tool(
          name = "Search",
          func=tavily_tool,
          description="useful for when you need to answer questions about current events",
      ),
      Tool(
          name = "Toogle_Case",
          func = lambda word: toggle_case(word),
          description = "use when you want covert the letter to uppercase or lowercase",
      ),
      Tool(
          name = "Sort String",
          func = lambda string: sort_string(string),
          description = "use when you want sort a string alphabetically",
      ),

        ]

def toggle_case(word):
            toggled_word = ""
            for char in word:
                if char.islower():
                    toggled_word += char.upper()
                elif char.isupper():
                    toggled_word += char.lower()
                else:
                    toggled_word += char
            return toggled_word

def sort_string(string):
     return ''.join(sorted(string))

tool_executor = ToolExecutor(tools)