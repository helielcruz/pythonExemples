from random import randint

palpite = None
numero = randint(0,2)
while True:
    print("Qual o número correto: ")
    palpite = int(input())
    if palpite != numero:
        print('Errou!')
    else:
        print('Acertou!')
        break