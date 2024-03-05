
# tem tipos, só não precisa definir
# 1. numerico:
#   int, float, complex (não usa na aula, científico, pode pesquisar)

# int
idade = 10

# float
altura = 153.65

# 2. Bool
verdade = True
falso = False

# 3. Strings
# sequência de caracteres
nome = 'Maria da Silva'
nome = "Maria da Silva"

# multilinha
frase = """Olá Mundo
como está?
a
b
"""

# interpolação de Strings
nome = 'João'
idade = 17
frase = f"Olá {nome}, você tem {idade} anos!"
print(frase)

# e o char?
letra = 'a'
letra = "b"

# acessar caractere de strings
nome = 'Silvio Santos'
print (nome[0])
print (nome[-1])
print (nome[-3])

print (nome[0 : 3]) # os três primeiros caracteres

# Strings são objetos
# métodos
print (nome.capitalize())
print (nome.upper())

# 4. list (listas)
# lista de valores
# indexada
# pode ser alterada

habilidades = []
habilidades = ['html', 'php', 'java', 'javascript', 'python']

# acesso aos itens da lista
habilidades[1]

# se perguntar pode falar que pode ser uma tupla, uma lista, string 
# NÃo diga simples, que não da pra saber

# adicionar valores na lista
habilidades.append('C#')
print(habilidades)

# inserir em uma posição
habilidades.insert(1, 'css')
print(habilidades)

# retirar os dados do array
# habilidades.clear()
print(habilidades)

# iterar a lista
for habilidade in habilidades:
    print (habilidade, end=', ')

def somar (n1, n2):
    return n1 + n2

somar (10.0, 23.9)
somar (n1 = 2, n2 = 5)
somar (n2 = 1, n1 = 3) 
# vira tipo um valor padrao se não passar param.
# pode colocar valor em qqr ordem

# 5.tuple (tupla)
# 'lista' de valores
# não pode ser alterada

tupla = ('sim', 'não', 'talvez', 'se quiser sim')
print (tupla[3])


# set (conjunto)
# conjunto de valores
# não permite elementos duplicados
# não é indexdado

habilidades = {'python', 'java', 'html','html'}
print (habilidades)

# 7. dict (dicionario)
# palavra -> definição
# chave -> valor
# key -> value
# conjunto chave valor

nome  = 'Pedro Alves'
idade = 17
habilidades = ['Java', 'C#', 'CSS']
empregado = True

candidato = {
    'nome': 'Pedro Alves',
    'idade': 17,
    'habilidades': ['Java', 'C#', 'CSS'],
    'empregado': True
}

print (candidato['nome'])
print (candidato.values())
print (candidato.keys())

# 8. None
#   null
# é um tipo, literal específico
# para definir variável sem valor

nome = None

