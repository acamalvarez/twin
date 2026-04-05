from collections.abc import Generator

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from google import genai

from app.models.chat import ChatRequest
from app.services.chat_gemini import get_chat_stream, get_genai_client

router = APIRouter()


@router.post("/")
async def chat(request: ChatRequest, client: genai.Client = Depends(get_genai_client)) -> StreamingResponse:
    response = get_chat_stream(request.message, client)

    def generate() -> Generator[str, None, None]:
        for chunk in response:
            if chunk.text is not None:
                yield chunk.text

    return StreamingResponse(generate())


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}
