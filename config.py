"""
=========================================================
IS-U Smart Assistant
Configuration centrale de l'application
=========================================================
"""

from pathlib import Path


# =========================================================
# Répertoires du projet
# =========================================================

ROOT_DIR = Path(__file__).parent

DATA_DIR = ROOT_DIR / "data"

UPLOAD_DIR = DATA_DIR / "uploads"

VECTOR_DB_DIR = DATA_DIR / "vector_db"

LOG_DIR = DATA_DIR / "logs"


# =========================================================
# LLM
# =========================================================

OLLAMA_MODEL = "llama3:8b"

OLLAMA_HOST = "http://localhost:11434"


# =========================================================
# Interface
# =========================================================

APP_NAME = "IS-U Smart Assistant"

VERSION = "0.1.0"

DEFAULT_LANGUAGE = "fr"


# =========================================================
# Documents
# =========================================================

SUPPORTED_EXTENSIONS = [
    ".xml",
    ".pdf",
    ".docx",
    ".xlsx",
    ".csv",
    ".json",
]