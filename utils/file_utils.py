"""
Helper functions for file system operations.
"""

import os

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)
