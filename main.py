import math
import random
import string
import sys


def gerar_senha():

    from_input = input("Qual o tamanho da senha que quer gerar: ")
    if from_input == 'c':
        exit(0)
    try:
        tamanho = int(from_input)
        print('transformou em int')
    except ValueError:
        print('Não é um número inteiro. Tente novamente ou c para sair')

    tudo = string.printable
    symbolos = tudo[62:-6]
    numeros = tudo[0:10]
    letras = tudo[10:62]
    dictescolha = {1: letras, 2: numeros, 3: symbolos}
    let, num, sym = [], [], []
    escolhas = []

    while len(sym) <= math.ceil(tamanho / 3):
        sym.append(random.choice(symbolos))
        print("Colocando o Símbolo")
    while len(let) <= math.ceil(tamanho / 4):
        print("Colocando Letra")
        let.append(random.choice(letras))
    while len(num) <= math.floor(tamanho / 4):  # problema aqui
        print("Colocando Número")
        num.append(random.choice(numeros))
    escolhas = [sym + let + num]
    escolhas = escolhas[0]
    print(escolhas)
    random.shuffle(escolhas)


    senha = ''.join(escolhas)
    print(''.join(escolhas))


if __name__ == '__main__':
    gerar_senha()