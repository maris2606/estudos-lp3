
# OBS - essa forma importa tudo do módulo
import matematica
# cuidado com importação circular

n1 = 5
n2 = 2

print()
print(matematica.somar(n1, n2))
print(matematica.subtrair(n1, n2)) # funções
print(matematica.PI) # constantes

# -------------------------------------------------------------
# importar coisas específicas - MELHOR - fica mais legível... já sabe o que foi usado
from matematica import PI, somar, subtrair

n1 = 5
n2 = 2

# acesso direto ao nome da função
print()
print(somar(n1, n2))
print(subtrair(n1, n2))
print(PI)

# -------------------------------------------------------------
# importar todos, mas sem digitar modulo. (import)
from matematica import *

n1 = 5
n2 = 2

# acesso direto ao nome da função
print()
print(somar(n1, n2))
print(subtrair(n1, n2))
print(PI)


# -------------------------------------------------------------
# é dificil de ver, ocorre mais com função
from matematica import PI as PI_mat, somar as mais_mais, subtrair 

# se já tiver uma var com mesmo nome?
PI = 3.14
# ou usa o modulo. (import)
# ou usa o as [nome diferente/ apelido]

n1 = 5
n2 = 2

# acesso direto ao nome da função
print()
print(mais_mais(n1, n2))
print(subtrair(n1, n2))
print(PI)
print(PI_mat)

# -------------------------------------------------------------
# modulo com 100 funções diferentes, com diferentes usos
# separaria em varios módulos
# então usa pacote pra agrupar esses módulos
# é uma pasta

# pacote sempre estará num diretorio

# acessa o pacote e navega os módulos com '.'
from estatistica.descritiva import media
from estatistica.inferencial import VALOR

valores = [10, 9]

print(media(valores))
print(VALOR)


# não é muito boa prática sair da pasta 
# from ..matematica import soma