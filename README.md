# Acalmo API

Acalmo API is a modular, high-performance FastAPI application designed to scale across multiple AI-driven domains and objectives. Its primary module provides a streaming digital twin chat interface using the Google Gemini AI SDK via Vertex AI.

## Features

- **Multi-Objective Architecture:** Fully modularized routing (e.g., `/api/v1/...`) to gracefully handle future expansions beyond the base digital twin.
- **Asynchronous Streaming:** Provides a real-time, async streaming chat interface using the `gemini-3-flash-preview` model.
- **Vertex AI Backend:** Seamless integration natively with Google Cloud Vertex AI infrastructure.
- **Easy Configuration:** Uses Pydantic `BaseSettings` for robust environment-based deployment.
- **Health Verification:** Built-in global health endpoint for Load Balancers and proxies.

## Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) for package management
- Google Cloud Platform credentials configured for Vertex AI

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/acamalvarez/acalmo-api.git
    cd acalmo-api
    ```

2.  **Configure environment variables:**
    Ensure you have authenticated your local environment with Application Default Credentials (ADC) via Google Cloud SDK:
    ```bash
    gcloud auth application-default login
    ```
    Create a `.env` file in the root directory if you need to override the configured project/location.

3.  **Install dependencies:**
    ```bash
    uv sync
    ```

## Running the application

Start the FastAPI development server:

```bash
uv run fastapi dev .\app\main.py
```
*(For production use: `uv run uvicorn app.main:app --host 0.0.0.0 --port 8080`)*

You can then access the interactive documentation at:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

- `POST /api/v1/twin/chat`: Accepts a standard JSON payload `{"message": "string"}` and streams asynchronous message chunks back utilizing the digital twin logic.
- `GET /health`: Returns the current health status of the application global scope.

## Testing

Run the heavily-mocked test suite using pytest via uv:

```bash
uv run pytest tests
```
