palpite = 0
numero = 9
while palpite != numero:
    print("Qual o número correto: ")
    palpite = int(input())
    if palpite != numero:
        print('Errou!')
else:
    print("Acertou!")

