fatorial = 1
result = 0

numero = int(input("Insira um número: "))

if numero < 0:
    print('Não existe fatorial de numeros negativos')
elif numero == 0:
    print(f'O fatorial de {numero} é 1.')
else:
    for x in range(1, numero+1):
        fatorial *= x
        print(fatorial)
