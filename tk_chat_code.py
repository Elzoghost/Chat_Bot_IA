import os
from dotenv import load_dotenv
from openkey import openai_api_key
from chat_code import CodeGenerator
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import openai
import requests
import json


# Utiliser la clé API OpenAI
openai.api_key = openai_api_key


class CodeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Code Generator")

        # Set background and foreground colors
        master.configure(bg="black")
        self.question_label_fg = "white"
        self.question_field_fg = "white"
        self.language_label_fg = "white"
        self.language_field_fg = "white"
        self.output_area_bg = "white"
        self.output_area_fg = "black"

        # Create input labels and fields
        self.question_label = tk.Label(master, text="Posez votre question liée à la programmation : ", fg=self.question_label_fg, bg="black")
        self.question_label.pack()
        self.question_field = tk.Entry(master, fg=self.question_field_fg, bg="black")
        self.question_field.pack()

        self.language_label = tk.Label(master, text="Dans quelle langage souhaitez-vous générer du code ? (Python, Java, JavaScript, HTML, CSS, C, C++, Matlab, Scilab, SQL, MongoDB, Hadoop) : ", fg=self.language_label_fg, bg="black")
        self.language_label.pack()
        self.language_field = tk.Entry(master, fg=self.language_field_fg, bg="black")
        self.language_field.pack()

        # Create generate button
        self.generate_button = tk.Button(master, text="Générer du code", command=self.generate_code, bg="white")
        self.generate_button.pack()

        # Create output text area
        self.output_area = ScrolledText(master, height=20, bg=self.output_area_bg, fg=self.output_area_fg)
        self.output_area.pack()

        # Create instance of CodeGenerator class
        self.generator = CodeGenerator()

    def generate_code(self):
        # Get user input
        question = self.question_field.get()
        language = self.language_field.get()

        # Construct prompt for code generation
        prompt = (f"Générer du code {language} pour : {question}\n\n")

        # Call function to generate code
        generated_code = self.generator.generate_code(prompt, language)

        # Clear output area and display generated code
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, generated_code)

# Create tkinter window
root = tk.Tk()

# Create instance of CodeGeneratorGUI class
app = CodeGeneratorGUI(root)

# Run tkinter event loop
root.mainloop()
