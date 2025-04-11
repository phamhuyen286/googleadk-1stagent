from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import Session
from google.adk.memory import InMemoryMemoryService
from dotenv import load_dotenv
from agents import root_agent  # Updated import
import logging

logging.basicConfig(level=logging.DEBUG)

load_dotenv('./.env')

APP_NAME = "First Application To Test"
USER_ID = "user_1"
SESSION_ID = "session_001"

session_service = InMemoryMemoryService()
session = Session(
    app_name=APP_NAME,
    user_id=USER_ID,
    id=SESSION_ID
)
session_service.add_session_to_memory(session)

try:
    runner_root = Runner(
        app_name=APP_NAME,
        session_service=session_service,
        agent=root_agent
    )
    logging.info("Runner initialized successfully!")
except Exception as e:
    logging.error(f"Error initializing runner: {e}")
    raise