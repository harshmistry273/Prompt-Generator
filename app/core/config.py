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

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# OBJECT
settings = Settings()
