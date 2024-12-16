import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import PhotoImage

class ShowResults(tk.Toplevel):
    def __init__(self, parent, resultado=None):
        super().__init__(parent)
        self.resultado = resultado
        self.setup_window()
        self.show_results()

    def setup_window(self):
        self.title("Resultado do Sorteio")
        self.geometry("300x450")
        self.resizable(False, False)
        self.attributes("-topmost", True)

    def show_results(self):

        self.label = tk.Label(self, text="Resultado do Sorteio", font=("Comic Sans MS", 16, "bold"))
        self.label.pack(anchor="center")

        self.label = tk.Label(self, text="--------------------", font=("Comic Sans MS", 16, "bold"))        
        self.label.pack(anchor="center")

        for pessoa, amigo_secreto in self.resultado.items():
            self.label = tk.Label(self, text=f"{pessoa} -> {amigo_secreto}", font=("Comic Sans MS", 12, "italic"))
            self.label.pack()