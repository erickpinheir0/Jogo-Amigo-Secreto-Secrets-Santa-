import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import PhotoImage

class EntryWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # Configurar janela
        self.title("Entrada de Dados")
        self.geometry("800x600")
        self.resizable(False, False)

        style = ttk.Style()
        style.configure("Custom.TEntry", 
        font=("Comic Sans MS", 16, "bold"), 
        foreground="black", 
        background="white")

        self.entry = ttk.Entry(self, style="Custom.TEntry")
        # Centralizando o entry na janela
        self.entry.place(relx=0.5, rely=0.25, relwidth=0.3, relheight=0.1, anchor="center")

        self.entry.focus_set()