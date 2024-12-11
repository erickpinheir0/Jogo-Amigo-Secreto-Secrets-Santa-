import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import PhotoImage

class ShowResults(tk.Toplevel):
    def __init__(self, parent, resultado):
        super().__init__(parent)
        self.resultado = resultado
        self.setup_window()
        self.show_results()

    def setup_window(self):
        self.title("Resultado do Sorteio")
        self.geometry("600x400")
        self.resizable(False, False)

    def show_results(self):

        for pessoa, amigo_secreto in self.resultado.items():
            label = tk.Label(self, text=f"{pessoa} -> {amigo_secreto}")
            label.pack()
        
