import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import PhotoImage


class EntryWindow(tk.Toplevel):
    def __init__(self, parent):

        # Construtor da classe pai
        super().__init__(parent)
        self.parent = parent
        
        # Configurar janela 
        self.title("Entrada de Dados")
        self.geometry("350x120+600+500")  
        self.resizable(False, False)

        # Configurar estilo da entrada
        style = ttk.Style()
        style.configure("Custom.TEntry",
            justify="center", 
            foreground="black", 
            background="white")
        
        # Configurar estilo do botão
        style.configure("Confirm.TButton",
            font=("Comic Sans MS", 14, "bold"),
            justify="center",
            relx=0.5,
            rely=0.8,
            relwidth=0.3,
            relheight=0.75,
            anchor="center"
            )

        # Texto e estilo do label
        label_text = "Quantas pessoas irão participar do jogo?"
        self.label = ttk.Label(self, text=label_text, font=("Comic Sans MS", 12, "italic"))
        self.label.place(relx=0.53, rely=0.2, relwidth=1, relheight=0.3, anchor="center")

        # Campo de entrada
        self.entry = ttk.Entry(self, style="Custom.TEntry", font=("Arial", 14, "italic"), justify="center")
        self.entry.place(relx=0.5, rely=0.5, relwidth=0.55, relheight=0.25, anchor="center")

        # Botão de confirmar
        self.confirm_button = ttk.Button(
            self,
            text="Confirmar",
            style="Confirm.TButton",
            command=self.confirmar
        )
        self.confirm_button.place(relx=0.5, rely=0.8, relwidth=0.3, relheight=0.30, anchor="center")
        self.entry.focus_set()
        
        # Variável para armazenar o resultado
        self.total_pessoas = None

    # Função para confirmar o número de participantes
    def confirmar(self):
        """Confirma o número de participantes e fecha a janela"""
        try:
            valor = int(self.entry.get())
            if valor > 0:
                self.total_pessoas = valor
                self.destroy()
            else:
                messagebox.showerror("Erro", "Por favor, insira um número maior que zero!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido!")