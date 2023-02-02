""" def reduzirNum(numInt):
    while numInt > 0:
        print(numInt)
        numInt -=1


reduzirNum(10) """


def reduzirNum(numInt):  # Exemplo de recursão
    if numInt > 0:
        reduzirNum(numInt - 1)
        print(numInt)


reduzirNum(10)