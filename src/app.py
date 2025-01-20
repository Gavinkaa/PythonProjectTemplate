import logging
from example import add

logger = logging.getLogger(__name__)


if __name__ == "__main__":

    LOG_FORMAT = "[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d] %(message)s"
    DATE_FORMAT = "%H:%M:%S"

    # Set up basic configuration for the root logger
    # This will affect all loggers that don't have their own handlers.
    logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

    # Set up logging for specific modules
    # logging.getLogger("matplotlib").setLevel(logging.WARNING)

    logger.info("Starting the application")

    print(f"2 + 3 = {add(2, 3)}")
