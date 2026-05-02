# Use a python image
FROM python:3.14-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.4.15 /uv /uvx /bin/

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Set working directory.
WORKDIR /app

# Copy the pyproject.toml and uv.lock.
COPY pyproject.toml uv.lock ./

# Install the project's dependencies using the lockfile and settings
RUN uv sync --frozen --no-install-project --no-dev

# Then, copy the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
COPY . /app
RUN uv sync --frozen --no-dev

# Using a smaller base image for the runtime
FROM python:3.14-slim

# Install uv for the runtime so we can use `uv run` as per project rules
COPY --from=ghcr.io/astral-sh/uv:0.4.15 /uv /uvx /bin/

# Set standard python environment variables for production
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Create a non-root user and group for security
RUN groupadd -r appgroup && useradd -r -m -g appgroup appuser

# Copy the application from the builder and set ownership
COPY --from=builder --chown=appuser:appgroup /app /app

# Switch to the non-root user
USER appuser

# Expose the port (Cloud Run sets the PORT env var, defaults to 8080)
EXPOSE 8080

# Run the application using uvicorn.
# We use sh -c to allow environment variable substitution for $PORT, which is required by Cloud Run.
CMD ["sh", "-c", "uv run uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
