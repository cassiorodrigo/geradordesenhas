from random import randint
import string


def gerar_senha():

    from_input = input("Qual o tamanho da senha que quer gerar: ")
    if from_input == 'c':
        exit(0)
    try:
        tamanho = int(from_input)
    except ValueError:
        print('Não é um número inteiro. Tente novamente ou c para sair')
        gerar_senha()

    tudo = string.printable
    symbolos = tudo[62:-6]
    numeros = tudo[0:10]
    letras = tudo[10:62]
    dictescolha = {1: letras, 2: numeros, 3: symbolos}
    senha = []
    novasenha = ''
    while len(senha) < tamanho:
        tipochar = randint(1,3)
        if tipochar == 1:
            poschar = randint(0,52)
        elif tipochar == 2:
            poschar = randint(0,10)
        elif tipochar == 3:
            poschar = randint(0,32)
        charactere = dictescolha[tipochar][poschar]
        print(charactere)
        senha.append(charactere)
    novasenha = ''.join(str(e) for e in senha)
    print(novasenha)
    senha = []

if __name__ == '__main__':
    gerar_senha()