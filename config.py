"""
Configuration settings for the IS-U Smart Assistant.
"""

import os
from dotenv import load_dotenv

load_dotenv()

SAP_CONFIG = {
    "client": os.getenv("SAP_CLIENT", "100"),
    "user": os.getenv("SAP_USER", ""),
    "password": os.getenv("SAP_PASSWORD", ""),
    "host": os.getenv("SAP_HOST", ""),
    "sysnr": os.getenv("SAP_SYSNR", "00"),
}

LLAMA_API_URL = os.getenv("LLAMA_API_URL", "http://localhost:11434")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
