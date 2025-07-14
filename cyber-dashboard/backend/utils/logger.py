"""Application logger configuration."""

import logging
from logging.handlers import RotatingFileHandler


def get_logger() -> logging.Logger:
    """Return configured logger."""
    logger = logging.getLogger("cyber-dashboard")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(
            "app.log", maxBytes=1024 * 1024, backupCount=3
        )
        console = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        console.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(console)
    return logger


