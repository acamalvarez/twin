from unittest.mock import MagicMock

from pytest_mock import MockerFixture

from app.core.config import config
from app.services.chat_gemini import client as genai_client
from app.services.chat_gemini import get_chat_stream


def test_config_defaults() -> None:
    # Verify that config loads with the expected default value
    assert config.model == "gemini-3-flash-preview"


def test_get_chat_stream(mocker: MockerFixture) -> None:
    # Mock the client.models.generate_content_stream call
    mock_chunk = MagicMock()
    mock_chunk.text = "Mocked AI response"

    # mocker.patch.object to mock the stream method on the client instance
    mock_stream_method = mocker.patch.object(genai_client.models, "generate_content_stream", return_value=[mock_chunk])

    prompt = "Test prompt"
    stream = get_chat_stream(prompt)

    # Iterate over the mock stream to verify its content
    chunks = list(stream)
    assert len(chunks) == 1
    assert chunks[0].text == "Mocked AI response"

    # Ensure it was called with the correct parameters
    mock_stream_method.assert_called_once_with(
        model=config.model,
        contents=prompt,
    )


def test_get_chat_stream_error(mocker):
    import pytest
    from google.genai.errors import APIError

    # Mock the generate_content_stream to raise an exception
    mock_stream_method = mocker.patch.object(
        genai_client.models,
        "generate_content_stream",
        side_effect=APIError(code=500, response_json={"error": {"message": "API error"}}),
    )

    prompt = "Test prompt"

    with pytest.raises(APIError, match="API error"):
        get_chat_stream(prompt)

    # Ensure it was called with the correct parameters
    mock_stream_method.assert_called_once_with(
        model=config.model,
        contents=prompt,
    )
