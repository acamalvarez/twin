from collections.abc import Generator

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.chat import ChatRequest
from app.services.chat_gemini import get_chat_stream

router = APIRouter()


@router.post("/")
async def chat(request: ChatRequest) -> StreamingResponse:
    response = get_chat_stream(request.message)

    def generate() -> Generator[str, None, None]:
        for chunk in response:
            if chunk.text is not None:
                yield chunk.text

    return StreamingResponse(generate())


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "healthy"}
