import os
from dotenv import load_dotenv
from openkey import openai_api_key
import openai
from openai import api_key, Completion
import requests
import json


# Utiliser la clé API OpenAI
openai.api_key = openai_api_key

# Mapping des langages de programmation aux IDs des moteurs de génération de code correspondants
ENGINE_IDS = {
    "python": "davinci-codex",
    "java": "davinci-codex-java-002",
    "javascript": "davinci-codex-javascript-002",
    "html": "davinci-codex-html-002",
    "css": "davinci-codex-css-002",
    "c": "davinci-codex-c-002",
    "cpp": "davinci-codex-cpp-002",
    "matlab": "davinci-codex-matlab-002",
    "scilab": "davinci-codex-scilab-002",
    "sql": "davinci-codex-sql-002",
    "mongodb": "davinci-codex-mongodb-002",
    "hadoop": "davinci-codex-hadoop-002"
}

# Fonction pour générer du code à partir d'un prompt et d'un langage de programmation
def generate_code(prompt, language):
    # Appel de l'API OpenAI pour générer du code
    response = Completion.create(
        engine=ENGINE_IDS[language.lower()],
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extraction du code généré de la réponse de l'API
    generated_code = response.choices[0].text.strip()

    return generated_code

# Demander à l'utilisateur une question liée à la programmation et le langage de programmation souhaité
question = input("Posez votre question liée à la programmation : ")
language = input("Dans quelle langage souhaitez-vous générer du code ? (Python, Java, JavaScript, HTML, CSS, C, C++, Matlab, Scilab, SQL, MongoDB, Hadoop) : ")

# Exemples d'entrée et de sortie pour la question posée
input_examples = [
    "Comment trier une liste en Python ?",
    "Comment ajouter un élément à une liste en Python ?",
    "Comment trouver la somme de deux nombres en Python ?",
    "Comment lire un fichier en Python ?",
    "Comment créer une classe en Python ?"
]

output_examples = [
    "sorted_list = sorted(my_list)",
    "my_list.append(new_element)",
    "sum = num1 + num2",
    "with open('filename', 'r') as file:",
    "class MyClass:\n    def __init__(self):\n        pass"
]

# Construire le prompt pour la génération de code à partir des exemples d'entrée et de sortie
prompt = f"Generer du code {language} pour : {question}\n\nExemples:\n"

for input_example, output_example in zip(input_examples, output_examples):
    prompt += f"Input : {input_example}\nOutput : {output_example}\n"

# Appel de la fonction pour générer du code
generated_code = generate_code(prompt, language)

# Affichage du code généré
print(generated_code)
