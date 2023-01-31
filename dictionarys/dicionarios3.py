""" tupla = ("item", "item2", "item3")
dicio = dict.fromkeys(tupla)
print(dicio)
 """

""" tupla = ("item", "item2", "item3")
tupla2 = ("item", "item2", "item3")
dicio = dict.fromkeys(tupla, tupla2)
print(dicio) """

dicio = {
    "dicio1": {
        "nome": "Pedro",
    },
    "dicio2": {
        "nome": "Maria",
        "dicio3": {
            "dependentes": 3
        }
    }
}
print(dicio)