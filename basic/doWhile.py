palpite = 0
numero = 9
while True:
    print("Qual o número correto: ")
    palpite = int(input())
    if palpite != numero:
        print('Errou!')
    else:
        print('Acertou!')
        break
