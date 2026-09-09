from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: str = "dbpilot_user"
    POSTGRES_PASSWORD: str = "dbpilot_password"
    POSTGRES_DB: str = "dbpilot_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    APP_ENV: str = "development"
    APP_PORT: int = 8000
    GEMINI_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()