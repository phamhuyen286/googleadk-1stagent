def say_hello(name: str = "there") -> str:
    """
    Cung cấp lời chào đơn giản, có thể chào người dùng bằng tên.
    """
    print(f"--- Công cụ: say_hello được gọi với tên: {name} ---")
    return f"Xin chào, {name}!"

def say_goodbye() -> str:
    """
    Cung cấp lời chào tạm biệt đơn giản để kết thúc cuộc trò chuyện.
    """
    print(f"--- Công cụ: say_goodbye được gọi ---")
    return "Tạm biệt! Chúc bạn một ngày tốt lành."

def get_weather(city: str) -> dict:
    """
    Trả về báo cáo thời tiết hiện tại cho một thành phố được chỉ định.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "Thời tiết tại New York hiện đang nắng với nhiệt độ 25 độ C "
                "(41 độ Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "report": "Không tìm thấy dữ liệu thời tiết cho thành phố được yêu cầu."
        }