"""
IS-U Smart Assistant - Document Loader
Orchestrates loading documents from various formats.
"""


class DocumentLoader:
    """Unified document loader supporting multiple file formats."""

    def __init__(self):
        pass

    def load(self, file_path: str) -> str:
        """Load and extract text from a document."""
        raise NotImplementedError
