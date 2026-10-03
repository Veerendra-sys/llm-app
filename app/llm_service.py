import os
from ollama import chat

MODEL_NAME = os.getenv("MODEL_NAME", "qwen2.5:1.5b")


def generate_response(prompt: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.message.content
