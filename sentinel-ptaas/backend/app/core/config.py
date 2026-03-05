from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Sentinel PTaaS API"
    api_prefix: str = "/api/v1"
    secret_key: str = "change-me"
    access_token_expire_minutes: int = 60
    postgres_dsn: str = "postgresql+psycopg2://ptaas:ptaas@postgres:5432/ptaas"
    redis_url: str = "redis://redis:6379/0"
    minio_endpoint: str = "minio:9000"
    elasticsearch_url: str = "http://elasticsearch:9200"
    jira_base_url: str = ""
    jira_email: str = ""
    jira_api_token: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
