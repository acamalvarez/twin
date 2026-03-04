from typing import Optional

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(..., max_length=4096)
    session_id: Optional[str] = None
