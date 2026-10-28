import os
import dashscope
from dashscope import Generation
import asyncio

# 建议把 API Key 放在系统环境变量中，或者直接写在这里（仅限本地测试）
# 如果你直接在 Windows 终端设置了环境变量，这里就不需要显式赋值
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY", "sk-你的API_KEY填在这里")

class QwenClient:
    def __init__(self):
        # 这里可以设置系统提示词（人设）
        self.system_prompt = "你是一个名叫小智的儿童教育机器人。你性格温柔、有耐心，擅长用简单易懂的语言回答小朋友的问题，每次回答尽量不超过三句话。"

    async def chat(self, user_text: str) -> str:
        """
        异步调用 Qwen 模型进行对话
        """
        messages = [
            {'role': 'system', 'content': self.system_prompt},
            {'role': 'user', 'content': user_text}
        ]

        try:
            # dashscope 默认是同步阻塞的，为了不卡住 FastAPI，我们用 asyncio 包装一下
            # 在真实的生产环境中，可以使用 httpx 直接请求 HTTP 接口，或者使用 run_in_executor
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None,
                lambda: Generation.call(
                    model='qwen-turbo', # 推荐先用 qwen-turbo，速度快且便宜；如果追求智力可以换 qwen-max
                    messages=messages,
                    result_format='message'
                )
            )

            if response.status_code == 200:
                # 提取模型回复的文本
                reply = response.output.choices[0].message.content
                return reply
            else:
                print(f"调用 Qwen 失败: {response.code} - {response.message}")
                return "哎呀，我的大脑暂时连不上网了，请稍后再试。"

        except Exception as e:
            print(f"发生异常: {e}")
            return "哎呀，我刚刚走神了，没听清你说什么。"

# 实例化供外部调用
qwen_client = QwenClient()