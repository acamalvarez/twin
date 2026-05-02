# Acalmo API

Acalmo API is a modular, high-performance FastAPI application designed to scale across multiple AI-driven domains and objectives. Its primary module provides a streaming digital twin chat interface using the Google Gemini AI SDK via Vertex AI.

## Features

- **Multi-Objective Architecture:** Fully modularized routing (e.g., `/api/v1/...`) to gracefully handle future expansions beyond the base digital twin.
- **Asynchronous Streaming:** Provides a real-time, async streaming chat interface using the latest `gemini-2.5-flash` model.
- **Vertex AI Backend:** Seamless integration natively with Google Cloud Vertex AI infrastructure using Application Default Credentials (ADC).
- **Easy Configuration:** Uses Pydantic `BaseSettings` for robust environment-based deployment.
- **Dockerized Environment:** Fully containerized setup for easy local development and production deployments.
- **Automated CI/CD:** Ready-to-go deployment pipeline using Google Cloud Build, Artifact Registry, and Cloud Run, utilizing Secret Manager for sensitive environment variables.

## Prerequisites

- Python 3.14+ (or Docker)
- [uv](https://github.com/astral-sh/uv) for fast package management
- Google Cloud SDK (`gcloud`) configured for Vertex AI

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/acamalvarez/acalmo-api.git
    cd acalmo-api
    ```

2.  **Configure Google Cloud Credentials:**
    Ensure you have authenticated your local environment.
    ```bash
    gcloud auth application-default login
    ```

3.  **Environment Variables:**
    Create a `.env` file in the root directory and configure it with your project details and twin instructions:
    ```env
    GOOGLE_CLOUD_PROJECT=your-project-id
    GOOGLE_CLOUD_LOCATION=us-central1
    TWIN_INSTRUCTIONS="Your digital twin instructions here..."
    ```

## Running the application (Locally)

### Using Docker Compose (Recommended)
The project includes a `compose.yaml` file that automatically mounts your local codebase for live-reloading, and safely passes your host machine's Google Cloud ADC into the container.
```bash
docker compose up --build
```

### Using uv (Without Docker)
```bash
uv sync
uv run fastapi dev app/main.py --host 0.0.0.0 --port 8080
```

You can access the interactive documentation at:
- **Swagger UI:** [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)

## API Endpoints

- `POST /api/v1/twin/chat`: Accepts a standard JSON payload `{"message": "string"}` and streams asynchronous message chunks back utilizing the digital twin logic.
- `GET /health`: Returns the current health status of the application.

## CI/CD Deployment

The project contains a `cloudbuild.yaml` file that automates building and deploying the application to **Google Cloud Run**.

**Requirements:**
1. An Artifact Registry Docker repository.
2. A Secret Manager secret (e.g., `twin-instructions-secret`) containing your instructions.
3. IAM permissions assigned to the Cloud Build Service Account (`Cloud Run Admin`, `Service Account User`).

Once configured, pushing to the `main` branch will automatically trigger the deployment.

## Testing

Run the heavily-mocked test suite using pytest via uv:
```bash
uv run pytest tests
```
