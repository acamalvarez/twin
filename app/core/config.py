from google.genai.types import GenerateContentConfig
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    model: str = "gemini-2.5-flash"
    twin_instructions: str = ""

    @property
    def content_config(self) -> GenerateContentConfig:
        return GenerateContentConfig(
            temperature=0,
            top_p=0.95,
            top_k=40,
            system_instruction=self.twin_instructions,
        )


config = Config()
