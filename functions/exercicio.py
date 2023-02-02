"""
    Esse modulo verifica qual é o maior numero 
    e cria a média de dois valores
"""


def calcNum(x, y):
    media = (x+y)/2
    if x > y:
        return "O maior número eh: ", x, "e a media eh: ", media
    else:
        return "O maior numero eh: ", y, "e a media eh: ", media


calc = calcNum(5.5, 10.3)
print(calc)


def potCalc(base, expoente):
    result = base**expoente
    return "O resultado eh: ", result


calc = potCalc(5, 2)
print(calc)