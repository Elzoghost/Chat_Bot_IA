import os
from dotenv import load_dotenv
from openkey import openai_api_key
import openai
import requests
import json


# Utiliser la clé API OpenAI
openai.api_key = openai_api_key


class CodeGenerator:
    def __init__(self):
        self.engine_ids = {
            "python": "code-davinci-002",
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

    def generate_code(self, prompt, language):
        # Call OpenAI API to generate code
        response = openai.Completion.create(
            engine=self.engine_ids[language.lower()],
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Parse response and extract generated code
        generated_code = response.choices[0].text.strip()

        return generated_code








"""
# Define function to generate code
def generate_code(prompt, language):
    # Map language to corresponding engine ID
    engine_ids = {
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

    # Call OpenAI API to generate code
    response = openai.Completion.create(
        engine=engine_ids[language.lower()],
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Parse response and extract generated code
    generated_code = response.choices[0].text.strip()

    return generated_code

# Get user input
question = input("Posez votre question liée à la programmation : ")
language = input("Dans quelle langage souhaitez-vous générer du code ? (Python, Java, JavaScript, HTML, CSS, C, C++, Matlab, Scilab, SQL, MongoDB, Hadoop) : ")

# Construct prompt for code generation
prompt = (f"Générer du code {language} pour : {question}\n\n")

# Call function to generate code
generated_code = generate_code(prompt, language)

# Print generated code
print(generated_code)"""
