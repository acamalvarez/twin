from google.genai.types import GenerateContentConfig
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    model: str = "gemini-3-flash-preview"
    twin_instructions: str = ""
    cors_origins: list[str] = [
        "http://localhost:8001",
        "http://127.0.0.1:8001",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "https://acalmo.me",
    ]

    @property
    def content_config(self) -> GenerateContentConfig:
        return GenerateContentConfig(
            temperature=0,
            top_p=0.95,
            top_k=40,
            system_instruction=self.twin_instructions,
        )


config = Config()
