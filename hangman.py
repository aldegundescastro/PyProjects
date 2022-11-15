# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
    i_board = 0
    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.ind_board = 0

    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        # verifica se a letra degitada está presente na palavra
        if self.word.find(self.letter) > 0:
            print("letra encontrada !")
        else:
            self.ind_board += 1
            print("letra não encontrada !")



    # Método para verificar se o jogo terminou
    def hangman_over(self):
        print("hangman_over")
    # Método para verificar se o jogador venceu
    def hangman_won(self):
        print("hangman_won")
    # Método para não mostrar a letra no board
    def hide_word(self):
        print("hide_word")

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.ind_board])


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # cont referente ao número de chace (tamanho da palavra)
    cont = 0
    while cont <= len(game.word):
        # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        # Verifica o status do jogo
        game.print_game_status()
        letra = input("Digite uma letra: ")
        game.guess(letra)
        cont += 1
        # print(letra)

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()