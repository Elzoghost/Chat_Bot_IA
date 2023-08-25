
import os
import openai
from dotenv import load_dotenv
# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API OpenAI
openai_api_key = os.getenv("OPENAI_API_KEY")


