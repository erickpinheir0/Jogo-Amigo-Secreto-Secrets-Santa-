import random
import integrante
import secrets
import janela_principal


# Criando a lista de participantes
lista_participantes = secrets.criarLista()

# Exibindo a lista de participantes
secrets.exibirParticipantes(lista_participantes)

# Realizando o sorteio
resultado = secrets.sortearAmigoSecreto(lista_participantes)

# Exibindo o resultado do sorteio
secrets.exibirResultadoSorteio(resultado)

