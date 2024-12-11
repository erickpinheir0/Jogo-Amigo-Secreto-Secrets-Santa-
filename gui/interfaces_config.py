import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def gerarJanela():
    root = tk.Tk()
    root.title("Sorteio de Amigo Secreto")
    root.geometry("1380x900")
    root.resizable(False, False)

    # Carregar e configurar o background
    try:
        root.bg_image = PhotoImage(file="gui/images/background.png")
        bg_label = tk.Label(root, image=root.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        root.configure(bg='white')  

    return root.mainloop()

