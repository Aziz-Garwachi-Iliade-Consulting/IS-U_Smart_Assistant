"""
Détection des langues.
"""


class LanguageManager:

    @staticmethod
    def detect(text: str):

        text = text.lower()

        arabic = any("\u0600" <= c <= "\u06FF" for c in text)

        if arabic:
            return "ar"

        english_words = [
            "hello",
            "thanks",
            "please",
            "how",
            "what",
            "where",
        ]

        if any(word in text for word in english_words):
            return "en"

        return "fr"