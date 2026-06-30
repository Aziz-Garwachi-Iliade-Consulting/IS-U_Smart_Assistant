"""
Assistant principal.
"""

from chatbot.conversation_manager import ConversationManager
from chatbot.language_manager import LanguageManager
from services.ai_service import AIService


class Assistant:

    def __init__(self):

        self.ai = AIService()

        self.history = ConversationManager()

        self.language = LanguageManager()

    def ask(self, question: str):

        self.history.add_user_message(question)

        answer = self.ai.ask(question)

        self.history.add_assistant_message(answer)

        return answer