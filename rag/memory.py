"""
Manages conversation context memory for RAG.
"""

class RAGMemory:
    def __init__(self):
        self.context_items = []

    def add_context(self, document_id: str, content: str):
        self.context_items.append({"doc_id": document_id, "content": content})

    def get_combined_context(self) -> str:
        return "\n".join([item["content"] for item in self.context_items])
