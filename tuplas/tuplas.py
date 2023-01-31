""" tupla = ('item1', 'item2', 'item3', 'item1')

print(tupla)
print(len(tupla))
print(type(tupla))
print(tupla[2])

print(tupla.count('item1'))

tupla = ('item#', '5555', 'tttttt')
print(tupla) """

""" uf = ('item',)  # tuplas são definidas por parênteses e não por vírgula
print(type(uf)) """
lista = ['item1', 'item2', 'item3', 'item1']
tupla = ('item1', 'item2', 'item3', 'item1')
lista.append(tupla)

print(lista)

tupla = tuple(lista)
# del tupla
print(tupla)


