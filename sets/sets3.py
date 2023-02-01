""" conjunto = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}
# união dos conjuntos
conjunto3 = conjunto.union(conjunto2)
print(conjunto3) """

conjunto = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

# conjunto3 = conjunto.intersection(conjunto2) // recebe apenas os itens iguais nos dois sets
# conjunto3 = conjunto.symmetric_difference(conjunto2) // recebe apenas os itens diferentes nos dois conjuntos
conjunto.symmetric_difference(conjunto2)  # utiliza o mesmo conjunto para receber os itens diferentes
print(conjunto)