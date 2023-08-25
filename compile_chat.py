import os
from dotenv import load_dotenv
from openkey import openai_api_key
from chat_code import CodeGenerator
import openai
import requests
import json


# Utiliser la clé API OpenAI
openai.api_key = openai_api_key



# Get user input
question = input("Posez votre question liée à la programmation : ")
language = input("Dans quelle langage souhaitez-vous générer du code ? (Python, Java, JavaScript, HTML, CSS, C, C++, Matlab, Scilab, SQL, MongoDB, Hadoop) : ")

# Construct prompt for code generation
prompt = (f"Générer du code {language} pour : {question}\n\n")

# Create instance of CodeGenerator class
generator = CodeGenerator()

# Call function to generate code
generated_code = generator.generate_code(prompt, language)

# Print generated code
print(generated_code)
