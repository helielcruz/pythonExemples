# Adicionando elementos do set
""" set1 = {"item1", "item2", "item3"}
print(set1)
set1.add("Item5")
print(set1)
set1.add(8)
set1.add(True)
print(set1) """


""" set1 = {4, 9, 1, 5, 2}
set2 = {"item1", "item2", "item3"}
set1.update(set2)
print(set1) """

# Removendo elementos do set
set1 = {4, 9, 1, 5, 2, "item1", "item2", "item3"}
print(set1)

# set1.pop() // Remove aleatóriamente
# set1.remove("item3") // ocorre erro ao tentar remover item inexistente

set1.discard("item1")  # descarta item se existir
print(set1)

# del set1
set1.clear()  # apenas limpa o set
print(set1)