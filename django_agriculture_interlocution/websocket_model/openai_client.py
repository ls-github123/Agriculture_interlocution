import openai
import os
from decouple import config

class OpenAIClient:
    def __init__(self):
        self.api_key = config('OPENAI_API_KEY')  # 从环境变量获取 API 密钥
        openai.api_key = self.api_key

    async def stream_response(self, conversation):
        """
        调用 OpenAI API 并以生成的内容块流式返回
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # 使用您需要的模型
                messages=conversation,
                stream=True  # 启用流式响应
            )
            for chunk in response:
                if 'choices' in chunk:
                    delta = chunk['choices'][0]['delta']
                    if 'content' in delta:
                        yield delta['content']
        except Exception as e:
            print(f"OpenAI API 调用失败: {e}")
            yield "抱歉，无法生成回复。"