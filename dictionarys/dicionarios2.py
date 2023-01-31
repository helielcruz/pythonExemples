dicio = {"chave1": "Gabriel", "chave2": 1993, "chave3": True}
print(dicio)

dicio["chave1"] = "Pedro"
print(dicio["chave1"])
dicio.update({"estado": "SP"})
print(dicio)

# A função popitem() elimina o último item apenas da versão 3.7 e acima, abaixo disso é aleatório
dicio.popitem()
print(dicio)

dicio.pop("chave2")
print(dicio)

del dicio['chave3']
print(dicio)

dados = {"chave1": "Gabriel", "chave2": 1993, "chave3": True}

for x in dados.values():
    print(x)

ndicio = dados.copy()
print(ndicio)

ndicio2 = dict(dados)
print(ndicio2)