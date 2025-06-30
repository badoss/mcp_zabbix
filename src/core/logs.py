import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "mcp_server.log")

# Create logs directory if not exists
os.makedirs(LOG_DIR, exist_ok=True)

# Setup logger
logger = logging.getLogger("mcp_logger")
logger.setLevel(logging.INFO)

# File handler with rotation
file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(file_formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(file_formatter)

# Add handlers only once
if not logger.hasHandlers():
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
