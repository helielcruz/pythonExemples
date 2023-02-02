def impName(*nomes):  
    print(nomes)
    print(type(nomes))


lista = ['Luiz', 'Augusto', 'Pedro', 'João']
impName(*lista)  # Com * passa apenas os valores da lista
# Sem * passa a lista como uma coleção dentro da tupla criada como argumento 