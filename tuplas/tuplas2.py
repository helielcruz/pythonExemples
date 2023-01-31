tupla = ('item1', 'item2', 'item3')
tupla2 = ('a', 'b')

""" tupla = tupla * 3
print(tupla) """

""" for variavel in tupla:
    print(variavel)
 """
""" for x in range(len(tupla)):
    print(tupla[x]) """

(x, *y) = tupla

print(x)
print(y)
