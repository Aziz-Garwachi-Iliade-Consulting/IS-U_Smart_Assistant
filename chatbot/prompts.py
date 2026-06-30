"""
IS-U Smart Assistant - Prompt Templates
Defines prompt templates for the LLM interactions.
"""

SYSTEM_PROMPT = """You are an expert SAP IS-U assistant. 
You help users with questions about SAP IS-U processes, configurations, and troubleshooting.
Use the provided context to answer questions accurately."""

RAG_PROMPT_TEMPLATE = """Context:
{context}

Question: {question}

Answer:"""
