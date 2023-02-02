# Fatorial sem recursão
def fatorialS(num):
    fatorial = 1
    if num == 0:
        return 1
    else:
        for x in range(1, num + 1):
            fatorial *= x
        return fatorial


result = fatorialS(5)
print(result)


def fatorialR(num):  # Fatorial com recursão
    if num == 0:
        return 1
    else:
        return num * fatorialR(num - 1)


result = fatorialR(5)
print(result)