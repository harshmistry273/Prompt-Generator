# IMPORTS
from app.core.config import settings
import uvicorn


def main():
    """
        Main entry point for the FastAPI application.
    """
    uvicorn.run(
        app=settings.APP,
        port=settings.PORT,
        reload=settings.IS_DEV
    )


# ENTRYPOINT OF THE APPLICATION
if __name__ == "__main__":
    main()