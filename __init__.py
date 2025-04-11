from .greeting_agent import greeting_agent
from .farewell_agent import farewell_agent
from .root_agent import root_agent

# Define the main agent for the ADK to use
agent = root_agent

__all__ = ["greeting_agent", "farewell_agent", "root_agent", "agent"]