import random
import integrante
from fpdf import FPDF
from tkinter import Tk


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

def gerarPDF(resultado):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for pessoa, amigo_secreto in resultado.items():
        pdf.cell(200, 10, txt=f"{pessoa} -> {amigo_secreto}", ln=1, align="C")
    pdf.output("resultado.pdf")