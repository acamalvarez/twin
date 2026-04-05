from collections.abc import Iterator

from google import genai
from google.genai.types import GenerateContentResponse

from app.core.config import config


def get_genai_client() -> genai.Client:
    return genai.Client(api_key=config.google_api_key)


def get_chat_stream(prompt: str, client: genai.Client) -> Iterator[GenerateContentResponse]:
    stream: Iterator[GenerateContentResponse] = client.models.generate_content_stream(
        model=config.model,
        contents=prompt,
    )
    return stream
