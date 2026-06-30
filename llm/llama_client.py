"""
=========================================================
IS-U Smart Assistant
Client de communication avec Ollama
=========================================================
"""

from ollama import Client

from config import OLLAMA_HOST, OLLAMA_MODEL
from utils.logger import app_logger


class LlamaClient:
    """
    Client responsable de la communication avec Ollama.
    """

    def __init__(self):

        self.client = Client(host=OLLAMA_HOST)
        self.model = OLLAMA_MODEL

        app_logger.info("Client Ollama initialisé.")

    def health_check(self):
        """
        Vérifie que le serveur Ollama est disponible.
        """

        try:
            self.client.list()

            app_logger.info("Connexion à Ollama réussie.")

            return True

        except Exception as error:

            app_logger.error(f"Erreur Ollama : {error}")

            return False

    def list_models(self):
        """
        Retourne la liste des modèles disponibles.
        """

        try:

            models = self.client.list()

            return models

        except Exception as error:

            app_logger.error(error)

            return None

    def generate_response(self, prompt):
        """
        Génère une réponse avec le modèle Llama.
        """

        try:

            response = self.client.chat(

                model=self.model,

                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],

            )

            app_logger.info("Réponse générée avec succès.")

            return response["message"]["content"]

        except Exception as error:

            app_logger.error(error)

            return "Une erreur est survenue lors de la génération de la réponse."