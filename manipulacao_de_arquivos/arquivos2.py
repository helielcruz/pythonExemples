arquivo = open('manipulacao_de_arquivos/receita.txt')
#print(arquivo.closed)
# print(arquivo.read()) // lê tudo
""" print(arquivo.readline())  # Lê apenas a linha (Para quantas linhas for necessário)
print(arquivo.closed)
arquivo.close()
print(arquivo.closed) # Verifica se o arquivo está fechado. "Closed? True ou False" """

# Leitura de arquivo
""" with open('manipulacao_de_arquivos/receita.txt') as arquivo:
    print(arquivo.read())
    print(arquivo.closed)
print(arquivo.closed) """

# Escrita de arquivo // Sobrescreve
""" with open('manipulacao_de_arquivos/receita.txt', 'w') as arquivo:
    arquivo.write('Imaginação') """

# Incluir escrita
texto = """ 
    Estes modos são passados como segundo parâmetro do método open.
     Ou seja, se quisermos abrir um arquivo em modo de escrita,
      utilizamos a seguinte sintaxe:
 """ # 3 áspas dupplas permite ter quebra de linha auômática no texto
with open('manipulacao_de_arquivos/receita.txt', 'a') as arquivo:
    arquivo.write(texto)