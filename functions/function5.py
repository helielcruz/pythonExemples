""" def impName(nome, sobrenome, idade):
    print("nome:", nome)
    print("sobrenome:", sobrenome)
    print("idade:", idade)


impName(sobrenome="Augusto", nome="Luiz", idade=25) """


def impName(nome, sobrenome=None, idade=None):  
    print("nome:", nome)
    print("sobrenome:", sobrenome)
    print("idade:", idade)
    """ None torna a passagem de um parametro opcional
    Sempre deve estar após os parâmetros obrigatorios """


impName()
impName(sobrenome="Augusto", nome="Luiz", idade=25)