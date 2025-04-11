from google.adk.agents import Agent
from .greeting_agent import greeting_agent
from .farewell_agent import farewell_agent
from tools import get_weather  # Absolute import

root_agent = Agent(
    name="RootAgent",
    model="gemini-1.5-flash",
    description="Tác vụ điều phối chính. Xử lý các yêu cầu về thời tiết và phân công cho các tác vụ phụ.",
    instruction="Bạn là Tác vụ Thời tiết chính (Main Weather Agent), chịu trách nhiệm điều phối một nhóm.\n"
                "Nhiệm vụ chính của bạn là điều hướng yêu cầu người dùng đến đúng tác vụ phụ.\n"
                "Chỉ sử dụng công cụ 'get_weather' cho các yêu cầu thời tiết cụ thể.\n"
                "Bạn có các tác vụ phụ chuyên biệt:\n"
                "1. 'greeting_agent': Xử lý các lời chào đơn giản như 'Hi', 'Hello'.\n"
                "2. 'farewell_agent': Xử lý các lời tạm biệt đơn giản như 'Bye', 'See you'.\n"
                "Phân tích yêu cầu của người dùng. Nếu đó là lời chào, chuyển đến 'greeting_agent'.\n"
                "Nếu là yêu cầu thời tiết, tự xử lý bằng cách sử dụng 'get_weather'.\n"
                "Nếu không thuộc các trường hợp trên, hãy phản hồi phù hợp hoặc cho biết bạn không thể xử lý.",
    tools=[get_weather],
    sub_agents=[greeting_agent, farewell_agent]
)