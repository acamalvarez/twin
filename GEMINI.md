# Project: Twin

## General instructions
- **Focus on streaming:** Prioritize streaming responses when implementing or modifying AI features.
- **Async-first:** Use asynchronous patterns (`async`/`await`) for all API and AI service logic.
- **Pydantic-based configuration:** Manage all environment variables and configuration settings using Pydantic `BaseSettings`.

## Security
- **Input Validation:** Use Pydantic's `Annotated` and `StringConstraints` to strictly validate all incoming user messages (e.g., `min_length`, `max_length`, `strip_whitespace`).
- **Secret Management:** Never hardcode secrets. Always use environment variables managed via `BaseSettings`.
- **Non-root containers:** Ensure the `Dockerfile` always runs the application as a non-root user for production safety.

## Coding style
- **Indentation:** Use 4 spaces for Python code.
- **Type hinting:** Always include type hints for function arguments and return values.
- **FastAPI conventions:** Follow standard FastAPI patterns for routing, dependency injection, and request/response models.

## Containerization
- **Dockerfile:** Use multi-stage builds and `uv` for efficient, secure, and fast image generation.
- **Docker Compose:** Maintain a `compose.yaml` for local development, utilizing volume mounts for live-reloading.

## Testing
- **Test-driven development (TDD):** Prioritize writing tests before implementation when possible.
- **Unit and integration tests:** Use `pytest` for all tests. Use `TestClient` from FastAPI for testing API endpoints.
- **Mocking:** Use `pytest-mock` (mocker) to mock all external AI services and dependencies to ensure fast and deterministic tests.

## Development Workflow
- **Run Development Server:** `uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8080`
- **Run Tests:** `$env:PYTHONPATH = '.'; uv run pytest tests`
- **Install Dependencies:** `uv sync`
- **Docker Build:** `docker build -t twin-app .`
- **Docker Compose Up:** `docker compose up`
