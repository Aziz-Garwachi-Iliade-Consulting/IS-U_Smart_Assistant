"""
=========================================================
Logger central
=========================================================
"""

from loguru import logger

from config import LOG_DIR

LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.add(
    LOG_DIR / "assistant.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO",
)

app_logger = logger