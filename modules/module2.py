""" from random import *

print(randint(1,5))  # Gera um numero aleatório determinado """

from pacote import principal, secundario
# from pacote.more import outro as modulo
from pacote.more.outro import cubica


print(principal.soma(2, 3))
print(secundario.quadratica(5))
print(cubica(3))
