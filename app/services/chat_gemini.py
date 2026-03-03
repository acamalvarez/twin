from google import genai
from app.core.config import config

client = genai.Client(api_key=config.google_api_key)


def get_chat_stream(prompt: str):
    return client.models.generate_content_stream(
        model=config.model,
        contents=prompt,
    )
