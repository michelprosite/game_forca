import random
from os import system, name

letras_erradas = []
chance = 0
palavras = ['uva', 'banana', 'laranja']

# Função para limpar tela
def limpa_tela():
    # Para limpar a tela caso seja windows
    if name == 'nt':
        _=system('cls')
    # Para limpar a tela caso seja Mac ou Linux
    else:
        _=system('clear')


# Mensagem de boas vindas
print("*" * 40)
print("\n Seja bem vindo ao jogo da forca_V1 \n")
print("*" * 40)

def game():