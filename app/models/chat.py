from typing import Annotated

from pydantic import BaseModel, StringConstraints


class ChatRequest(BaseModel):
    message: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=4096),
    ]
    session_id: str | None = None
