"""
IS-U Smart Assistant - Vector Store
Manages the ChromaDB vector store for document embeddings.
"""


class VectorStore:
    """ChromaDB-backed vector store for document embeddings."""

    def __init__(self, persist_directory: str = "data/chroma_db"):
        self.persist_directory = persist_directory

    def add_documents(self, documents: list) -> None:
        """Add documents to the vector store."""
        raise NotImplementedError

    def query(self, query_text: str, n_results: int = 5) -> list:
        """Query the vector store for similar documents."""
        raise NotImplementedError
