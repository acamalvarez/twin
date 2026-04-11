import functools
from collections.abc import AsyncIterator

from google import genai
from google.genai.types import GenerateContentResponse

from app.core.config import config


@functools.cache
def get_genai_client() -> genai.Client:
    return genai.Client(vertexai=True)


async def get_chat_stream(prompt: str, client: genai.Client) -> AsyncIterator[GenerateContentResponse]:
    stream = await client.aio.models.generate_content_stream(
        model=config.model,
        contents=prompt,
        config=config.content_config,
    )
    return stream
