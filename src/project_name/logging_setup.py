import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Determine log level from environment or default to INFO
env_level = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_LEVEL = getattr(logging, env_level, logging.INFO)


def setup_logger(name: str = None, log_file: str = None, level: int = LOG_LEVEL):
    """
    Configure and return a logger that logs to both console and a rotating file handler.
    """
    logger_name = name or __name__
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Prevent adding handlers multiple times
    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s [%(filename)s:%(funcName)s] %(message)s"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler
        if log_file:
            log_path = Path(log_file)
        else:
            # Go up 3 levels: src/project_name/ -> src/ -> project_root/
            project_root = Path(__file__).resolve().parent.parent.parent
            logs_dir = project_root / "logs"
            logs_dir.mkdir(exist_ok=True)
            log_path = logs_dir / "app.log"
        file_handler = RotatingFileHandler(
            log_path, maxBytes=10 * 1024 * 1024, backupCount=5
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# Default logger for the package
logger = setup_logger("project_name")
