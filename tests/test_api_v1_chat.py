from unittest.mock import MagicMock
import pytest


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_chat_stream(client, mocker):
    # Mock get_chat_stream to return a sequence of chunks
    mock_chunk1 = MagicMock()
    mock_chunk1.text = "Hello"
    mock_chunk2 = MagicMock()
    mock_chunk2.text = " world!"
    
    mock_get_chat_stream = mocker.patch(
        "app.api.v1.chat.get_chat_stream", 
        return_value=[mock_chunk1, mock_chunk2]
    )
    
    payload = {"message": "Test message"}
    response = client.post("/", json=payload)
    assert response.status_code == 200
    # StreamingResponse is collected as a single response in TestClient
    assert response.text == "Hello world!"
    mock_get_chat_stream.assert_called_once_with("Test message")


def test_chat_empty_prompt(client):
    """Test that an empty prompt or whitespace-only prompt returns a 422 error."""
    # Test empty string
    payload_empty = {"message": ""}
    response_empty = client.post("/", json=payload_empty)
    assert response_empty.status_code == 422
    assert "String should have at least 1 character" in response_empty.text

    # Test whitespace string
    payload_whitespace = {"message": "   "}
    response_whitespace = client.post("/", json=payload_whitespace)
    assert response_whitespace.status_code == 422
    assert "String should have at least 1 character" in response_whitespace.text
