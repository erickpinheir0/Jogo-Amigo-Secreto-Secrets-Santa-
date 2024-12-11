import random
from logical import integrante
import secrets
import janela_principal
import interface

# Cria e executa a interface
interface = criar_interface()
interface.run()

# Criando a lista de participantes
lista_participantes = secrets.criarLista()

# Exibindo a lista de participantes
secrets.exibirParticipantes(lista_participantes)

# Realizando o sorteio
resultado = secrets.sortearAmigoSecreto(lista_participantes)

# Exibindo o resultado do sorteio
secrets.exibirResultadoSorteio(resultado)
