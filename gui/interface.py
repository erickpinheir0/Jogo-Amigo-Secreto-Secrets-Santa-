import entry_window
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

class Interface:
    def __init__(self):
        # Inicializa a janela principal
        self.root = tk.Tk()
        self.setup_window()
        self.setup_background()
        self.setup_icons()  # Adicionando a chamada do método
        self.create_widgets()
        
    def setup_window(self):
        """Configura as propriedades básicas da janela"""
        self.root.title("Sorteio de Amigo Secreto")
        self.root.geometry("1380x900+0+0")
        self.root.resizable(False, False)
    
    def setup_background(self):
        """Configura o background da janela"""
        try:
            self.bg_image = PhotoImage(file="gui/images/background.png")
            self.bg_label = tk.Label(self.root, image=self.bg_image)  # Salvando como atributo da classe
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Erro ao carregar background: {e}")  # Adicionando print do erro
            self.root.configure(bg='white')
    
    def setup_icons(self):
        """Configura os ícones da interface"""
        
        try:
            self.icon = PhotoImage(file=f"gui/images/novo.png")
            self.icon_label1 = tk.Label(self.root, image=self.icon)  # Salvando como atributo da classe
            self.icon_label2 = tk.Label(self.root, image=self.icon)  # Salvando como atributo da classe
            self.icon_label3 = tk.Label(self.root, image=self.icon)  # Salvando como atributo da classe
            self.icon_label4 = tk.Label(self.root, image=self.icon)  # Salvando como atributo da classe

            self.icon_label1.place(x=0, y=0, relwidth=0.145, relheight=0.2)  # Posição específica na tela
            self.icon_label2.place(x=1200, y=0, relwidth=0.145, relheight=0.2)
            self.icon_label3.place(x=0, y=725, relwidth=0.145, relheight=0.2)
            self.icon_label4.place(x=1200, y=725, relwidth=0.145, relheight=0.2)
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")  # Adicionando print do erro
    
    def create_widgets(self):
        """Cria os widgets da interface"""
        try:
            # Configurar estilo do botão
            style = ttk.Style()
            style.configure(
                "Custom.TButton",
                font=("Comic Sans MS", 16, "bold"),
                background="lightgreen",
            )

            self.open_button = ttk.Button(
                self.root,
                text="Iniciar Amigo Secreto",
                style="Custom.TButton",
                command=self.open_entry_window
            )
            self.open_button.place(relx=0.40, rely=0.45, relwidth=0.2, relheight=0.075)
        except Exception as e:
            print(f"Erro ao criar botão: {e}")

    def open_entry_window(self):
        """Abre a janela secundária"""
        new_window = entry_window.EntryWindow(self.root)
    
    def run(self):
        """Inicia o loop principal da interface"""
        self.root.mainloop()

# Função para criar e retornar uma instância da interface
def criar_interface():
    interface = Interface()
    return interface