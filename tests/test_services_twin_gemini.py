from collections.abc import AsyncGenerator
from unittest.mock import AsyncMock, MagicMock

import pytest
from pytest_mock import MockerFixture

from app.core.config import config
from app.services.twin_gemini import get_chat_stream, get_genai_client


def test_config_defaults() -> None:
    # Verify that config loads with the expected default value
    assert config.model == "gemini-3-flash-preview"


@pytest.mark.asyncio
async def test_get_chat_stream() -> None:
    mock_client = MagicMock()
    mock_chunk = MagicMock()
    mock_chunk.text = "Mocked AI response"

    async def mock_generate() -> AsyncGenerator[MagicMock, None]:
        yield mock_chunk

    mock_client.aio.models.generate_content_stream = AsyncMock(return_value=mock_generate())

    prompt = "Test prompt"
    stream = await get_chat_stream(prompt, mock_client)

    # Iterate over the mock stream to verify its content
    chunks = [chunk async for chunk in stream]
    assert len(chunks) == 1
    assert chunks[0].text == "Mocked AI response"

    # Ensure it was called with the correct parameters
    mock_client.aio.models.generate_content_stream.assert_called_once_with(
        model=config.model,
        contents=prompt,
        config=config.content_config,
    )


def test_get_genai_client(mocker: MockerFixture) -> None:
    # Clear the cache before the test to ensure clean state
    get_genai_client.cache_clear()

    # Mock the genai.Client class
    mock_client_cls = mocker.patch("app.services.twin_gemini.genai.Client")

    # First call
    client1 = get_genai_client()

    # Verify the mock was called correctly
    mock_client_cls.assert_called_once_with(vertexai=True)
    assert client1 == mock_client_cls.return_value

    # Second call to verify caching
    client2 = get_genai_client()

    # Verify the mock was NOT called again
    mock_client_cls.assert_called_once()
    assert client1 is client2

    # Clear the cache after the test
    get_genai_client.cache_clear()


@pytest.mark.asyncio
async def test_get_chat_stream_error() -> None:
    from google.genai.errors import APIError

    mock_client = MagicMock()

    mock_client.aio.models.generate_content_stream = AsyncMock(
        side_effect=APIError(code=500, response_json={"error": {"message": "API error"}})
    )

    prompt = "Test prompt"

    with pytest.raises(APIError, match="API error"):
        await get_chat_stream(prompt, mock_client)

    # Ensure it was called with the correct parameters
    mock_client.aio.models.generate_content_stream.assert_called_once_with(
        model=config.model,
        contents=prompt,
        config=config.content_config,
    )
