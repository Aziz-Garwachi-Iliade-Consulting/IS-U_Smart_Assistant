"""
Manages LLM prompts and dynamic templates.
"""

class PromptManager:
    def __init__(self):
        pass

    def get_system_prompt(self, context: str = "") -> str:
        return f"You are a helpful SAP IS-U Smart Assistant. Context: {context}"
