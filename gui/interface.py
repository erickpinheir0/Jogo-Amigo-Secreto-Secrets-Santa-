from gui.entry_window import EntryWindow
from gui.show_results import ShowResults
from logical.integrante import Integrante
from logical.secrets import sortearAmigoSecreto
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter as tk
import secrets

class Interface:

    # Inicializa a janela principal
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_background()
        self.setup_icons()  # Adicionando a chamada do método
        self.create_widgets()
        self.lista_participantes = []
        
    def setup_window(self):
        """Configura as propriedades básicas da janela"""
        self.root.title("Sorteio de Amigo Secreto")
        self.root.geometry("1380x900")
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

        # Texto e estilo do label
        label = tk.Label(self.root, text="SECRETS SANTA - AMIGO SECRETO", font=("Comic Sans MS", 24, "bold"), bg="darkred", fg="white")
        label.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.075, anchor="center")

        # Configurar estilo do botão
        style = ttk.Style()
        style.configure(
            "Custom.TButton",
            font=("Comic Sans MS", 16, "bold"),
            background="lightgreen",
        )

        self.open_button = ttk.Button(
            self.root,
            text="Iniciar Jogo",
            style="Custom.TButton",
            command=self.open_entry_window
        )
        self.open_button.place(relx=0.40, rely=0.45, relwidth=0.2, relheight=0.075)

        self.results = ttk.Button(
            self.root,
            text="Últimos Sorteios",
            style="Custom.TButton",
            command=self.perform_draw
        )
        self.results.place(relx=0.40, rely=0.55, relwidth=0.2, relheight=0.075)

        self.quit_button = ttk.Button(
            self.root,
            text="Sair",
            style="Custom.TButton",
            command=self.root.quit
        )
        self.quit_button.place(relx=0.40, rely=0.65, relwidth=0.2, relheight=0.075)

    def open_entry_window(self):
        """Abre a janela secundária"""
        new_window = EntryWindow(self.root)
        new_window.wait_window()
        if hasattr(new_window, 'total_pessoas') and new_window.total_pessoas:
            self.open_button.destroy()
            self.results.destroy()
            self.quit_button.destroy()
            self.total_pessoas = new_window.total_pessoas
            self.insert_participants()

    def insert_participants(self):
        """Inserir participantes na interface"""
        for i in range(self.total_pessoas):
            label_name = ttk.Label(self.root, text=f"Nome do Participante: ", font=("Comic Sans MS", 16, "bold"))
            label_value = ttk.Label(self.root, text=f"Valor Inserido: ", font=("Comic Sans MS", 16, "bold"))
            label_email = ttk.Label(self.root, text=f"Email: ", font=("Comic Sans MS", 16, "bold"))

            label_name.place(relx=0.5, rely=0.3 , relwidth=0.2, relheight=0.05, anchor="center")
            label_value.place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.05, anchor="center")
            label_email.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.05, anchor="center")

            entry_name = ttk.Entry(self.root, justify="center", font=("Arial", 14, "italic"))
            entry_value = ttk.Entry(self.root, justify="center", font=("Arial", 14, "italic"))
            entry_email = ttk.Entry(self.root, justify="center", font=("Arial", 14, "italic"))
            entry_name.focus_set()

            entry_name.place(relx=0.5, rely=0.35, relwidth=0.2, relheight=0.05, anchor="center")
            entry_value.place(relx=0.5, rely=0.45, relwidth=0.2, relheight=0.05, anchor="center")
            entry_email.place(relx=0.5, rely=0.55, relwidth=0.2, relheight=0.05, anchor="center")

            confirm_participant = ttk.Button(
                self.root,
                text="Confirmar",
                style="Custom.TButton",
                command=lambda: self.add_participant(entry_name, entry_value, entry_email)
            )
            confirm_participant.place(relx=0.5, rely=0.65, relwidth=0.2, relheight=0.075, anchor="center")

    def add_participant(self, entry_name, entry_value, entry_email):

        name = entry_name.get()
        value = entry_value.get()
        email = entry_email.get()
        participant = Integrante(name, value, email)

        if not participant.getNome() or not participant.getValor() or not participant.getEmail():
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return 
        
        self.lista_participantes.append(participant)

        entry_name.delete(0, tk.END)
        entry_value.delete(0, tk.END)
        entry_email.delete(0, tk.END)

        if len(self.lista_participantes) == self.total_pessoas:
                self.create_draw_button()

    def create_draw_button(self):
        self.draw_button = ttk.Button(
            self.root,
            text="Realizar Sorteio",
            command=self.perform_draw
        )
        self.draw_button.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.05, anchor="center")

    def perform_draw(self):
        resultado = sortearAmigoSecreto(self.lista_participantes)
        self.exibir_resultado(resultado)

    def exibir_resultado(self, resultado):
        show_results = ShowResults(self.root, resultado)

    def run(self):
        """Inicia o loop principal da interface"""
        self.root.mainloop()
