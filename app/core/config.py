from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Find My Service API"
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost:3306/find_my_service"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
