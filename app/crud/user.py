# IMPORTS
from app.core.logging import logger
from app.database.connection import SupaBaseConnection
from app.exceptions.database_exceptions import DataBaseException

from fastapi import HTTPException, status


class UserCRUD:
    # CLASS VARIABLES
    _client = SupaBaseConnection.get_client()

    # CLASS METHODS
    
    # GET USER BY EMAIL
    @classmethod
    def get_user_by_email(cls, email: str):
        try:
            logger.info("Getting user by email")
            response = (
                cls._client.table("users")
                .select("*")
                .eq(column="email", value=email)
                .execute()
            )

            if not response.data:
                logger.info("No user found")
                return False

            return response.data

        except Exception as e:
            raise DataBaseException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=f"An error occured: {str(e.message)}",
            )

    # INSERT USER
    @classmethod
    def create_user(cls, user_data: dict):
        try:
            response = cls._client.table("users").insert(user_data).execute()

            return response.data

        except Exception as e:
            raise DataBaseException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=f"An error occured: {str(e.message)}",
            )
