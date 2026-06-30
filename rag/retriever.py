"""
IS-U Smart Assistant - Retriever
Retrieves relevant document chunks for a given query.
"""


class Retriever:
    """Retrieves relevant context from the vector store."""

    def __init__(self):
        pass

    def retrieve(self, query: str, top_k: int = 5) -> list:
        """Retrieve the top-k most relevant document chunks."""
        raise NotImplementedError
