from ollama import chat
from config import OLLAMA_MODEL

class LlamaChat:
    def get_response(self, user_input):
        response = chat(
            model=OLLAMA_MODEL,
            messages=[{'role': 'user', 'content': user_input}]
        )
        return response.message.content
