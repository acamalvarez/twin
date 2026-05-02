from google.genai.types import GenerateContentConfig
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    model: str = "gemini-2.5-flash"
    twin_instructions: str = ""
    cors_origins: str | list[str] = ""

    @field_validator("cors_origins", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str):
            return [i.strip() for i in v.split(",") if i.strip()]
        if isinstance(v, list):
            return v
        return []

    @property
    def content_config(self) -> GenerateContentConfig:
        return GenerateContentConfig(
            temperature=0,
            top_p=0.95,
            top_k=40,
            system_instruction=self.twin_instructions,
        )


config = Config()
