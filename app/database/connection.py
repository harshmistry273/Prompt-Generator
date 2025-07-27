# IMPORTS
from supabase import create_client, Client

from typing import Optional

from app.core.config import settings
from app.core.logging import logger

class SupaBaseConnection:
    # CLASS VARIABLES
    _client: Optional[Client] = None

    # CLASS METHODS
    @classmethod
    def initialize_client(cls):
        """
            creates a supabase client
        """
        cls._client = create_client(supabase_url=settings.SUPABASE_PROJECT_URL, supabase_key=settings.SUPABASE_ANON)
        logger.info("Supabase client initialized")

    @classmethod
    def get_client(cls):
        """
            gets supabase client
        """
        if cls._client is None:
            logger.warning("Supabase client not initialized, initializing one")
            cls.initialize_client()
        
        return cls._client

    @classmethod
    def reset_client(cls):
        """
            resets supabase client
        """
        cls._client = None
