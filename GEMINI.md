# Project: Twin

## General instructions
- **Focus on streaming:** Prioritize streaming responses when implementing or modifying AI features.
- **Async-first:** Use asynchronous patterns (`async`/`await`) for all API and AI service logic.
- **Pydances-based configuration:** Manage all environment variables and configuration settings using Pydantic `BaseSettings`.

## Coding style
- **Indentation:** Use 4 spaces for Python code.
- **Type hinting:** Always include type hints for function arguments and return values.
- **FastAPI conventions:** Follow standard FastAPI patterns for routing, dependency injection, and request/response models.

## Testing
- **Test-driven development (TDD):** Prioritize writing tests before implementation when possible.
- **Unit and integration tests:** Use `pytest` for all tests. Use `TestClient` from FastAPI for testing API endpoints.
- **Mocking:** Use `pytest-mock` (mocker) to mock all external AI services and dependencies to ensure fast and deterministic tests.
- **Command:** Execute tests with `$env:PYTHONPATH = '.'; uv run pytest tests`.
