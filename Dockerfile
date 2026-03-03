FROM python:3.14-rc-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:0.4.15 /uv /uvx /bin/

# Set working directory.
WORKDIR /app

# Copy the pyproject.toml and uv.lock.
COPY pyproject.toml uv.lock ./

# Install dependencies.
RUN uv sync --frozen --no-dev

# Copy the rest of the application code.
COPY . .

# Expose the port the app runs on.
EXPOSE 8080

# Command to run the application using uvicorn.
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
