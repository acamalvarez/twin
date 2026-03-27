from fastapi import FastAPI
from fastapi.routing import APIRoute

from app.main import app


def test_app_is_fastapi_instance() -> None:
    """Test that the app is an instance of FastAPI."""
    assert isinstance(app, FastAPI)


def test_app_has_routes() -> None:
    """Test that the app has the expected routes."""
    routes = [route.path for route in app.routes if isinstance(route, APIRoute)]
    assert "/" in routes
    assert "/health" in routes
