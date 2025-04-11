from google.adk.agents import Agent
from tools import say_goodbye  # Absolute import

farewell_agent = Agent(
    model="gemini-1.5-flash",
    name="farewell_agent",
    instruction="Bạn là một Tác vụ Tạm biệt (Farewell Agent). NHIỆM VỤ DUY NHẤT của bạn là đưa ra lời chào tạm biệt lịch sự.\n"
                "Sử dụng công cụ 'say_goodbye' khi người dùng cho biết họ sắp rời đi\n"
                "(ví dụ: sử dụng các từ như 'bye', 'goodbye', 'thanks bye', 'see you').\n"
                "Không thực hiện bất kỳ hành động nào khác.",
    description="Xử lý các lời chào tạm biệt đơn giản bằng cách sử dụng công cụ 'say_goodbye'.",
    tools=[say_goodbye],
)