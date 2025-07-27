# IMPORTS
import logging


# INITIALE LOGGER AND SET LEVEL
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# INITIATE CONSOLE LEVEL LOGGER AND ADD FORMAT
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(lineno)d - %(message)s"
    )
)


# ADD TO LOGGER
logger.addHandler(console_handler)
