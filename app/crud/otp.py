# IMPORTS
from app.core.logging import logger
from app.database.connection import client
from app.exceptions.database_exceptions import DataBaseException

from fastapi import HTTPException, status


class OTPCRUD:
    # CLASS METHODS

    # INSERT USER
    @classmethod
    def create_otp(cls, otp_data: dict):
        try:
            response = client.table("otp").insert(otp_data).execute()

            return response.data

        except Exception as e:
            raise DataBaseException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                message=f"An error occured: {str(e.message)}",
            )
