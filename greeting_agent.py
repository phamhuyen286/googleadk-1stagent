from google.adk.agents import Agent
from tools import say_hello  # Absolute import

greeting_agent = Agent(
    model="gemini-1.5-flash",
    name="greeting_agent",
    instruction="Bạn là một Tác vụ Chào hỏi (Greeting Agent). NHIỆM VỤ DUY NHẤT của bạn là cung cấp lời chào thân thiện.\n"
                "Sử dụng công cụ 'say_hello' để tạo ra lời chào.\n"
                "Nếu người dùng cung cấp tên, hãy chắc chắn truyền nó cho công cụ.\n"
                "Không tham gia vào bất kỳ cuộc hội thoại hoặc tác vụ nào khác.",
    description="Xử lý các lời chào đơn giản bằng cách sử dụng công cụ 'say_hello'.",
    tools=[say_hello],
)