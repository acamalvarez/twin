from collections.abc import AsyncGenerator
from unittest.mock import MagicMock

from fastapi.testclient import TestClient
from pytest_mock import MockerFixture


def test_health_check(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_chat_stream(client: TestClient, mocker: MockerFixture) -> None:
    # Mock get_chat_stream to return a sequence of chunks
    mock_chunk1 = MagicMock()
    mock_chunk1.text = "Hello"
    mock_chunk2 = MagicMock()
    mock_chunk2.text = " world!"

    async def mock_generate() -> AsyncGenerator[MagicMock, None]:
        yield mock_chunk1
        yield mock_chunk2

    mock_get_chat_stream = mocker.patch("app.api.v1.endpoints.twin.get_chat_stream", return_value=mock_generate())

    payload = {"message": "Test message"}
    response = client.post("/api/v1/twin/chat", json=payload)
    assert response.status_code == 200
    # StreamingResponse is collected as a single response in TestClient
    assert response.text == "Hello world!"
    mock_get_chat_stream.assert_called_once_with("Test message", mocker.ANY)


def test_chat_stream_missing_text_chunk(client: TestClient, mocker: MockerFixture) -> None:
    # Mock get_chat_stream to return a sequence of chunks including one with None text
    mock_chunk1 = MagicMock()
    mock_chunk1.text = "Hello"
    mock_chunk2 = MagicMock()
    mock_chunk2.text = None
    mock_chunk3 = MagicMock()
    mock_chunk3.text = " world!"

    async def mock_generate() -> AsyncGenerator[MagicMock, None]:
        yield mock_chunk1
        yield mock_chunk2
        yield mock_chunk3

    mock_get_chat_stream = mocker.patch("app.api.v1.endpoints.twin.get_chat_stream", return_value=mock_generate())

    payload = {"message": "Test message"}
    response = client.post("/api/v1/twin/chat", json=payload)
    assert response.status_code == 200
    # StreamingResponse is collected as a single response in TestClient
    # The chunk with None text should be ignored
    assert response.text == "Hello world!"
    mock_get_chat_stream.assert_called_once_with("Test message", mocker.ANY)
