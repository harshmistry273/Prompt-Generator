# IMPORTS
from pydantic_settings import BaseSettings, SettingsConfigDict


# CLASS TO MANAGE ENV. VARIABLES
class Settings(BaseSettings):
    # ENVIRONMENT
    APP: str
    PORT: int
    IS_DEV: bool
    
    # DATABASE
    SUPABASE_PROJECT_URL: str
    SUPABASE_ANON: str
    
    # UTILITY
    SECRET_KEY: str
    ALGORITHM: str
    EXPIRES_MINUTES: int
    
    # EMAIL
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM: str
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool
    USE_CREDENTIALS: bool
    USE_CREDENTIALS: bool

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# OBJECT
settings = Settings()
