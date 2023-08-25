"""import openai
import PySimpleGUI as sg
import os
from dotenv import load_dotenv
from openkey import openai_api_key
import openai
import requests
import json


# Utiliser la clé API OpenAI
openai.api_key = openai_api_key

class QABot:
    def __init__(self, keybot):
        
        self.keybot = keybot
        self.theme = sg.theme('LightBlue2')
        self.layout = [[sg.Text('Posez une question :', size=(20, 1)), sg.InputText(size=(60,1))],
                  [sg.Button('Obtenir la réponse'), sg.Button('Quitter')]]
        self.window = sg.Window('Assistant de question-réponse', self.layout,size=(800, 200))
        
        

    def generate_answer(self, prompt, model, max_tokens):
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
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quitter':
                break
            if event == 'Obtenir la réponse':
                question = values[0]
                prompt = f"Q: {question}\nA:"
                answer = self.generate_answer(prompt, "davinci", 100)
                sg.PopupNonBlocking(answer,title='Réponse')
                self.window['Obtenir la réponse'].Update('Poser une autre question')
                
                

                while True:
                    event, values = self.window.read()
                    if event == sg.WINDOW_CLOSED or event == 'Quitter':
                        break
                    if event == 'Obtenir la réponse':
                        question = values[0]
                        prompt = f"Q: {question}\nA:"
                        answer = self.generate_answer(prompt, "davinci", 100)
                        sg.PopupNonBlocking(answer,title='Réponse')

        self.window.close()

if __name__ == '__main__':
    bot = QABot(openai.api_key)
    bot.run()
"""
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

class QABot:
    def __init__(self, keybot):
        
        self.keybot = keybot
        self.theme = sg.theme('LightBlue2')
        self.layout = [[sg.Text('Posez une question :', size=(20, 1)), sg.InputText(size=(60,1), key='question')],
                       [sg.Button('Obtenir la réponse'), sg.Button('Quitter')],
                       [sg.Output(size=(100,400), font=('Helvetica', 10), key='output')]]
        self.window = sg.Window('Assistant de question-réponse', self.layout, size=(1000, 600))
        
    def generate_answer(self, prompt, model, max_tokens):
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
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Quitter':
                break
            if event == 'Obtenir la réponse':
                question = values['question']
                prompt = f"Q: {question}\nA:"
                answer = self.generate_answer(prompt, "davinci", 100)
                print(f"Q: {question}\n")
                print(f"A: {answer}\n")
                self.window['question'].update('')
                
        self.window.close()

if __name__ == '__main__':
    bot = QABot(openai.api_key)
    bot.run()
