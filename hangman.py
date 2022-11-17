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

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.wordlist = list(self.word.strip())  # string para lista
        self.palavra = ['_']
        self.ind_board = 0  # indice do board
        self.cont_inicio = 0

    # Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        # verifica se a letra degitada está presente na string
        # substitui '_' pela letra encontrada em palavra e substitui a letra por '_' em wordlist
        if self.wordlist.count(self.letter):
            self.palavra[self.wordlist.index(self.letter)] = self.letter
            self.wordlist[self.wordlist.index(self.letter)] = '_'
        else:
            self.ind_board += 1

            print("Letra não encontrada !")

    # Método para não mostrar a letra no board
    def hide_word(self):
        if self.cont_inicio == 0:
            self.cont_inicio = 1
            self.palavra.clear()
            for i in self.word:
                self.palavra.append("_")
        print("Palavra: ", self.palavra)


    # Método para verificar se o jogo terminou
    def hangman_over(self):
        print(self.ind_board)
        return self.hangman_won() or self.ind_board == 6

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if self.palavra.count('_') == 0:
            return True
        else:
            return False

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
    while not game.hangman_over():
        # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
        # Verifica o status do jogo
        game.print_game_status()
        game.hide_word()
        letra = input("Digite uma letra: ")
        game.guess(letra)
    game.print_game_status()
    game.hide_word()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word.upper())

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()