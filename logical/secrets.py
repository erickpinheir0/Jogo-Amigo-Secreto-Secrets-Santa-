import random
import json
import tkinter as tk

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
