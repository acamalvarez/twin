from collections.abc import AsyncGenerator

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from google import genai

from app.models.twin import ChatRequest
from app.services.twin_gemini import get_chat_stream, get_genai_client

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest, client: genai.Client = Depends(get_genai_client)) -> StreamingResponse:
    response = await get_chat_stream(request.message, client)

    async def generate() -> AsyncGenerator[str, None]:
        async for chunk in response:
            if chunk.text is not None:
                yield chunk.text

    return StreamingResponse(generate(), media_type="text/event-stream")
