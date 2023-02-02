"""Esse modulo tem como objetivo retornar
se um numero é primo ou não"""

numero = int(input("Insira um numero para saber se ele é primo: "))

if numero > 1:
    for x in range(1, numero):
        if (numero % x) == 0:
            print("Esse não é um numero primo! ")
            break
        else:
            print("Esse é um numero primo!")
            break
else:
    print('Esse número não é primo: Numero menor ou igual à 1')
