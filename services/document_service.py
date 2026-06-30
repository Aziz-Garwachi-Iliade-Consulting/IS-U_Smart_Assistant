"""
Interface service for document ingestion and preprocessing.
"""

class DocumentService:
    def __init__(self, loader):
        self.loader = loader

    def process_document(self, file_path: str):
        return []
