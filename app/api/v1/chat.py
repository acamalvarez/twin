from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.services.chat_gemini import get_chat_stream
from app.models.chat import ChatRequest

router = APIRouter()


@router.post("/")
async def chat(request: ChatRequest):
    response = get_chat_stream(request.message)

    def generate():
        for chunk in response:
            yield chunk.text

    return StreamingResponse(generate())


@router.get("/health")
async def health():
    return {"status": "healthy"}
