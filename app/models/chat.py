from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints


class ChatRequest(BaseModel):
    message: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    message: str
    session_id: Optional[str] = None
