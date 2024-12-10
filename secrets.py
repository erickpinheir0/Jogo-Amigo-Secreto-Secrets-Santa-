import random
import integrante
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
from tkinter import ttk

import json

def abrirJanela():
    janela = tk.Tk()
    janela.title("Amigo Secreto")
    janela.geometry("400x300")
    janela.mainloop()

totalPessoas = int(input("Insira o número de pessoas que irão participar do amigo secreto: "))

def criarLista():
    lista_participantes = []
    for i in range(totalPessoas):
        print(f"Participante {i + 1}/{totalPessoas}")
        nome = input("Insira o nome da pessoa: ")
        valor = input("Insira o valor que a pessoa irá depositar: ")
        email = input("Insira o email da pessoa: ")
        participante = integrante.Integrante(nome, valor, email)
        lista_participantes.append(participante)

    return lista_participantes

def exibirParticipantes(lista):
    print("\n=== Lista de Participantes ===")
    contador = 1
    for participante in lista:
        print(f"\nParticipante {contador}:")
        print(participante)
        contador += 1
    print("\n===========================")

def sortearAmigoSecreto(lista_participantes):

    nomes = [participante.getNome() for participante in lista_participantes]    
    sorteados = nomes.copy()
    
    random.shuffle(sorteados)
    
    
    for i in range(len(nomes)):
        if nomes[i] == sorteados[i]:
            
            proximo = (i + 1) % len(nomes)
            sorteados[i], sorteados[proximo] = sorteados[proximo], sorteados[i]
    
    
    resultado_sorteio = {}
    for i in range(len(nomes)):
        resultado_sorteio[nomes[i]] = sorteados[i]
    
    return resultado_sorteio

def exibirResultadoSorteio(resultado):
    print("\n=== Resultado do Sorteio ===")
    for pessoa, amigo_secreto in resultado.items():
        print(f"{pessoa} -> {amigo_secreto}")
    print("===========================")

