# Twin

Twin is a high-performance FastAPI application that provides a streaming chat interface using the Google Gemini AI SDK. You can use it to integrate advanced generative AI capabilities into your web services with minimal setup.

## Features

- **Streaming chat:** Provides a real-time chat interface using the `gemini-3-flash-preview` model.
- **FastAPI backend:** Leverages asynchronous programming for efficient request handling.
- **Easy configuration:** Uses Pydantic for robust environment-based configuration.
- **Health check:** Includes a built-in endpoint to monitor service status.

## Prerequisites

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) for package management
- A Google API Key for Gemini

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/twin.git
    cd twin
    ```

2.  **Configure environment variables:**
    Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

3.  **Install dependencies:**
    ```bash
    uv sync
    ```

## Running the application

Start the development server using uvicorn:

```bash
uv run uvicorn app.main:app --reload
```

You can then access the interactive documentation at:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API endpoints

- `GET /`: Streams a chat response from Gemini for a sample prompt.
- `GET /health`: Returns the current health status of the application.

## Testing

Run the test suite using pytest via uv:

```bash
$env:PYTHONPATH = '.'; uv run pytest tests
```

(Note: For Windows PowerShell use `$env:PYTHONPATH = '.'`, for Linux/macOS use `PYTHONPATH=.`).

## Documentation conventions

This `README.md` follows these documentation conventions:

- **Sentence case headings:** All headings use sentence case (e.g., "Documentation conventions").
- **Second person tone:** The documentation addresses you, the reader, directly using "you".
- **Present tense:** The text uses the present tense to describe the current state and actions.
- **Short and focused structure:** Paragraphs are kept concise and focused on a single topic.
- **Tagged code blocks:** All code blocks include language tags for proper syntax highlighting.
- **Practical examples:** Functional examples are provided for common tasks like installation and execution.
- **Google Developer Documentation Style Guide:** The overall style aligns with the standard Google developer documentation guidelines.
