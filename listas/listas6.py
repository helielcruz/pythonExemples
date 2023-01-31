lista = ['carro', 'barco', 'aviao', 'Helicóptero', 'hélice', 'astra', 'Azul']
lista.sort(key = str.lower)  # Ordena mesmo com inicio da string maiusculas e minúsculas
print(lista)

# lista.pop(0)
# lista.remove('barco')
# del lista[0:1]

carrinho = ['3', '8', '1']
# carrinho.sort()  # ordena em ordem alfabética e numérica crescente

# carrinho.sort(reverse = True) # decrescente

# carrinho.reverse()



print(carrinho)
# carrinho.clear()

for x in range(len(carrinho)):
    print(x, carrinho[x])