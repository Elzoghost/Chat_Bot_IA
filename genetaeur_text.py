import tkinter as tk
import openai
from openkey import openai_api_key

# Utiliser la clé API OpenAI
openai.api_key = openai_api_key

class OpenAIInterface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.prompt_label = tk.Label(self, text="Entrez votre idée ou consigne : ")
        self.prompt_label.pack()
        self.prompt_entry = tk.Entry(self)
        self.prompt_entry.pack()
        self.generate_button = tk.Button(self, text="Générer", command=self.generate_text)
        self.generate_button.pack()
        self.generated_text_label = tk.Label(self, text="Voici le texte généré : ")
        self.generated_text_label.pack()
        self.generated_text_frame = tk.Frame(self, bd=1, relief="solid") # ajouter une bordure autour du texte généré
        self.generated_text_frame.pack()
        self.generated_text = tk.Label(self.generated_text_frame, text="", width=60, height=15, wraplength=500) # augmenter la taille du label contenant le texte généré
        self.generated_text.pack()
        self.quit_button = tk.Button(self, text="Quitter", command=root.quit)
        self.quit_button.pack()
        self.pack()

    def generate_text(self):
        prompt = self.prompt_entry.get()
        completions = openai.Completion.create(
            engine="curie", # utilise le modèle curie pour une réponse plus créative
            prompt=prompt,
            max_tokens=2000, # génère une réponse plus longue
            n=1,
            stop=None,
            temperature=0.7, # ajuste la créativité de la réponse
        )
        message = completions.choices[0].text
        self.generated_text.config(text=message.strip())

root = tk.Tk()
root.geometry("700x500") # Redimensionner la fenêtre
app = OpenAIInterface(master=root)
app.mainloop()
