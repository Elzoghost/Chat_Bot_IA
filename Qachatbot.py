import openai
import PySimpleGUI as sg
import os
from dotenv import load_dotenv
from openkey import openai_api_key
import openai
import requests
import json

# Utiliser la clé API OpenAI
openai.api_key = openai_api_key


class OpenAI_QA:
    """
    Cette classe utilise l'API OpenAI pour fournir des réponses aux questions posées.
    """
    def __init__(self, keybot):
        """
        Initialise une nouvelle instance de la classe OpenAI_QA.

        :param api_key: La clé API OpenAI.
        """
        self.keybot = keybot
        

    def generate_answer(self, question, model, max_tokens=1000):
        """
        Génère une réponse à partir d'une question donnée.

        :param question: La question posée.
        :param model: Le modèle à utiliser pour générer la réponse.
        :param max_tokens: Le nombre maximum de jetons à générer.
        :return: La réponse générée.
        """
        prompt = f"Q: {question}\nA:"
        completions = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5,
            
        )
        message = completions.choices[0].text
        return message.strip()

    def run(self):
        """
        Démarre l'assistant de question-réponse.
        """
        sg.theme('LightBlue2')
        layout = [[sg.Text('Posez une question :', size=(20, 1)), sg.InputText(size=(60,1))],
                  [sg.Button('Obtenir la réponse'), sg.Button('Quitter')]]

        window = sg.Window('Assistant de question-réponse', layout, size=(800, 200))

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quitter':
                break
            if event == 'Obtenir la réponse':
                question = values[0]
                answer = self.generate_answer(question, "davinci", 100)
                sg.PopupNonBlocking(answer, title='Réponse')
                window['Obtenir la réponse'].Update('Poser une autre question')

                while True:
                    event, values = window.read()
                    if event == sg.WINDOW_CLOSED or event == 'Quitter':
                        break
                    if event == 'Obtenir la réponse':
                        question = values[0]
                        answer = self.generate_answer(question, "davinci", 100)
                        sg.PopupNonBlocking(answer, title='Réponse')

        window.close()


if __name__ == "__main__":
    bot = OpenAI_QA(openai.api_key)
    bot.run()
