# IMPORTS
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from app.core.logging import logger
from app.api.v1.users import router as user_router

# INITIALIZE APP
app = FastAPI(
    title="Prompt Engineering API",
    description="API for managing and executing prompt engineering tasks",
    version="0.0.0"
)


@app.get("/")
def check_health():
    """
        Health check endpoint to verify if the API is running.
    """
    logger.info("Health check endpoint called")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "Server is running!",
            "data": [],
            "status": True,
            "error": None
        }
    )


app.include_router(user_router)