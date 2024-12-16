
from gui.entry_window import EntryWindow
from gui.show_results import ShowResults
from logical.integrante import Integrante
from logical.secrets import sortearAmigoSecreto
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter as tk

class Interface:

    # Inicializa a janela principal
    def __init__(self, dados=None):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_background()
        self.setup_icons()  # Adicionando a chamada do método
        self.create_widgets()
        self.lista_participantes = []
        self.dados = dados
        self.resultado = self.dados
        
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
            command=lambda: self.exibir_ultimos_resultados(self.resultado)
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
        self.open_button.configure(state="disabled")

        self.new_window = EntryWindow(self.root)
        self.new_window.wait_window()
        if hasattr(self.new_window, 'total_pessoas') and self.new_window.total_pessoas:
            self.open_button.destroy()
            self.results.destroy()
            self.quit_button.destroy()
            self.total_pessoas = self.new_window.total_pessoas
            self.insert_participants()
        else: 
            self.open_button.configure(state="normal")

    def insert_participants(self):
        """Inserir participantes na interface"""
        for i in range(self.total_pessoas):

            string_name = f"Nome do Participante "
            string_value =f"Valor Inserido "
            string_email = f"Email: "
            string_fontLabel = ("Comic Sans MS", 16, "bold")
            string_fontEntry = ("Arial", 14, "italic")

            positionx = 0.5
            positiony = 0.3
            fillwidth = 0.2
            fillheight = 0.05
            align_center = "center"

            label_name = ttk.Label(self.root, text=string_name, font=string_fontLabel)
            label_value = ttk.Label(self.root, text=string_value, font=string_fontLabel)
            label_email = ttk.Label(self.root, text=string_email, font=string_fontLabel)

            label_name.place(relx=positionx, rely=positiony, relwidth=fillwidth, relheight=fillheight, anchor=align_center)
            label_value.place(relx=positionx, rely=positiony+0.1, relwidth=fillwidth, relheight=fillheight, anchor=align_center)
            label_email.place(relx=positionx, rely=positiony+0.2, relwidth=fillwidth, relheight=fillheight, anchor=align_center)

            self.entry_name = ttk.Entry(self.root, justify=align_center, font=string_fontEntry)
            self.entry_value = ttk.Entry(self.root, justify=align_center, font=string_fontEntry)
            self.entry_email = ttk.Entry(self.root, justify=align_center, font=string_fontEntry)

            self.entry_name.place(relx=positionx, rely=positiony+0.05, relwidth=fillwidth, relheight=fillheight, anchor=align_center)
            self.entry_value.place(relx=positionx, rely=positiony+0.15, relwidth=fillwidth, relheight=fillheight, anchor=align_center)
            self.entry_email.place(relx=positionx, rely=positiony+0.25, relwidth=fillwidth, relheight=fillheight, anchor=align_center)

            self.confirm_participant = ttk.Button(
                self.root,
                text="Confirmar",
                style="Custom.TButton",
                command=lambda: self.add_participant(self.entry_name, self.entry_value, self.entry_email)
            )
            self.insert_keys()
            self.confirm_participant.place(relx=0.5, rely=0.65, relwidth=0.2, relheight=0.075, anchor="center")

    def insert_keys(self):
        self.root.bind("<Return>", lambda event: self.confirm_participant.invoke())
        self.entry_name.focus_set()
        self.root.bind("<Up>", self.focus_up)
        self.root.bind("<Down>", self.focus_down)

    def focus_down(self, event):

        if self.entry_name.focus_get() == self.entry_name:
            self.entry_value.focus_set()
        elif self.entry_value.focus_get() == self.entry_value:
            self.entry_email.focus_set()
        elif self.entry_email.focus_get() == self.entry_email:
            self.entry_name.focus_set()

    def focus_up(self, event):
        if self.entry_email.focus_get() == self.entry_email:
            self.entry_value.focus_set()  # Loop para o último Entry
        elif self.entry_value.focus_get() == self.entry_value:
            self.entry_name.focus_set()
        elif self.entry_name.focus_get() == self.entry_name:
            self.entry_email.focus_set()

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
            style="Custom.TButton",
            command=self.perform_draw
        )
        self.play_again_button = ttk.Button(
            self.root,
            text="Jogar Novamente",
            style="Custom.TButton",
            command=self.jogar_novamente
        )

        self.draw_button.place(relx=0.5, rely=0.76, relwidth=0.2, relheight=0.05, anchor="center")
        self.play_again_button.place(relx=0.5, rely=0.84, relwidth=0.2, relheight=0.05, anchor="center")

    def perform_draw(self):
        self.resultado = sortearAmigoSecreto(self.lista_participantes)
        self.exibir_resultado(self.resultado)

    def exibir_resultado(self, resultado):
        self.draw_button.configure(state="disabled")
        self.show_results = ShowResults(self.root, resultado)
        self.show_results.wait_window()
        self.show_results.destroy()
        self.draw_button.configure(state="normal")
        self.dados = self.resultado

    def exibir_ultimos_resultados(self, resultado):
        self.results.configure(state="disabled")
        self.show_results = ShowResults(self.root, resultado)
        self.show_results.wait_window()
        self.show_results.destroy()
        self.results.configure(state="normal")

    def jogar_novamente(self):
        self.root.destroy()
        self.__init__(self.dados)

    def run(self):
        """Inicia o loop principal da interface"""
        self.root.mainloop()
