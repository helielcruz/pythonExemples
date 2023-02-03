#Paradigma imperativo

def Registrar(nome, idade, cpf, email):
    paciente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "email": email,
    }
    return paciente

# Paradigma orientado à objetos

""" 
classe - Um conjunto de objetos com as mesmas caracteristicas
objeto -  representação do mundo real como um tipo de dado de uma classe
Construtor - É a função com mesmo nome da classe
Atributo - São as variáveis de uma classe
"""

class Paciente:
    
    def __init__(self, nome, idade, cpf, email):  # com self chamando o construtor da mesma classe instanciada
        print("Acessando o construtor")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
