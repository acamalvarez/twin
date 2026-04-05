import pytest
from pydantic import ValidationError

from app.models.chat import ChatRequest


def test_chat_request_valid() -> None:
    """Test valid ChatRequest creation."""
    request = ChatRequest(message="Hello, world!", session_id="session-123")
    assert request.message == "Hello, world!"
    assert request.session_id == "session-123"


def test_chat_request_valid_no_session_id() -> None:
    """Test valid ChatRequest creation without session_id."""
    request = ChatRequest(message="Hello, world!")
    assert request.message == "Hello, world!"
    assert request.session_id is None


def test_chat_request_strip_whitespace() -> None:
    """Test that message whitespace is stripped."""
    request = ChatRequest(message="  Hello, world!  ")
    assert request.message == "Hello, world!"


def test_chat_request_empty_message() -> None:
    """Test validation fails for empty message."""
    with pytest.raises(ValidationError) as exc_info:
        ChatRequest(message="")
    assert "String should have at least 1 character" in str(exc_info.value)


def test_chat_request_whitespace_only_message() -> None:
    """Test validation fails for whitespace-only message (since it's stripped)."""
    with pytest.raises(ValidationError) as exc_info:
        ChatRequest(message="   ")
    assert "String should have at least 1 character" in str(exc_info.value)


def test_chat_request_message_too_long() -> None:
    """Test validation fails for message exceeding max_length."""
    long_message = "a" * 4097
    with pytest.raises(ValidationError) as exc_info:
        ChatRequest(message=long_message)
    assert "String should have at most 4096 characters" in str(exc_info.value)


def test_chat_request_missing_message() -> None:
    """Test validation fails when message is omitted."""
    with pytest.raises(ValidationError) as exc_info:
        ChatRequest()  # type: ignore
    assert "Field required" in str(exc_info.value)
