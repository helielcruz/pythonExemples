dicio = {"chave1": "Gabriel", "chave2": 1993, "chave3": True}

dicionario = {
    "nome": "Bruna",
    "idade": 27,
    "nacio": "Brasil"
}

print(dicionario['idade'])
print(dicionario.get('nacio'))
print(dicionario.keys())
print(len(dicio))
print(dicionario.values())

if "idade" in dicionario:
    print("Chave existente!")

print(dicionario.items())