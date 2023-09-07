import random
from os import system, name

# Função para limpar tela
def limpa_tela():
    # Para limpar a tela caso seja windows
    if name == 'nt':
        _=system('cls')
    # Para limpar a tela caso seja Mac ou Linux
    else:
        _=system('clear')


def game():
    limpa_tela()
    
    # iniciando a lista para listar as letras erradas
    letras_erradas = []
    # Iniciando a variavel de chances
    chances = 6
    # lIsta de palavras
    palavras = ['uva', 'banana', 'laranja', 'morango']

    # Sorteando a palavra
    palavra = random.choice(palavras)
    
    # Monta a extrutura oculta da palavra a ser descoberta
    letras_descobertas = ['_' for letra in palavra]

    # Mensagem de boas vindas
    print("*" * 40)
    print("\nSeja bem vindo ao jogo da forca_V1 \n")
    print(f"Advinhe a palavra abaixo, você terá {chances} chances antes de finalizar o jogo! \n")
    print("*" * 40)

    # Estrutura de loop do jogo
    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # tentativas
        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)
game()



