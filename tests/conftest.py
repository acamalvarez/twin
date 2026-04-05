from collections.abc import Iterator
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.chat_gemini import get_genai_client


@pytest.fixture
def client() -> Iterator[TestClient]:
    app.dependency_overrides[get_genai_client] = lambda: MagicMock()
    yield TestClient(app)
    app.dependency_overrides.clear()
