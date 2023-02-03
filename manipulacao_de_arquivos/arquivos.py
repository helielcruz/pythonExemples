import os

#Verifica se o arquivo existe
#print(os.path.exists('pastaNova/texto.py'))
print(os.path.exists('teste.txt'))

# Criando diretórios
#os.mkdir('manipulacao_de_arquivos/python')

#Criando arquivos no windows
open('manipulacao_de_arquivos/python/olamundo.py', 'w')
#os.remove('manipulacao_de_arquivos/teste.txt')
#os.remove('manipulacao_de_arquivos/pastaNova/texto.py')
#os.rmdir('manipulacao_de_arquivos/pastaNova')
os.rename('manipulacao_de_arquivos/python/olamundo.py', 'manipulacao_de_arquivos/python/ola.py')
""" 
#Criando arquivos no linux
os.mknod('olamundo.py')
"""

