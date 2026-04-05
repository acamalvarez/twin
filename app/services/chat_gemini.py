from google import genai
from app.core.config import config

client = genai.Client(vertexai=True)


def get_chat_stream(prompt: str):
    return client.models.generate_content_stream(
        model=config.model,
        contents=prompt,
        config=config.content_config,
    )
