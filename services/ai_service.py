"""
Service d'intelligence artificielle.
"""

from chatbot.prompt_manager import PromptManager
from llm.llama_client import LlamaClient


class AIService:

    def __init__(self):

        self.llm = LlamaClient()

        self.prompt_manager = PromptManager()

    def ask(self, user_message: str):

        prompt = (
            self.prompt_manager.get_system_prompt()
            + "\n\nUtilisateur :\n"
            + user_message
        )

        return self.llm.generate_response(prompt)