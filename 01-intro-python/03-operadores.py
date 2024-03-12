# operadores aritméticos
# + , - , *, /, %, **(potenciação)

nota1 = 10.0
nota2 = 6.0
nota3 = 8.0

media = (nota1 + nota2 + nota3) / 3

# potenciação
# 10 elevado ao quadrado

numero = 10**2
# equivalente ao 10 * 10
print(numero)


# operadores lógicos
# and, or, not
# ---
# devolve um boolean

print(True and True)
print(True and False)

print(False or True)
print(False or False)

print(not False)

# permite a entrada no sistema
# usuario não bloqueado E
# usuario é funcionario E
# hora atual entre 8h e 18h (dentro do horario comercial)
# ---
# caso for admin pode acessar de qualquer forma

usuario_bloqueado = False
usuario_funcionario = True
hora = 17
usuario_admin = False

horario_comercial = hora>8 and hora<18
funcionario_ativo = not usuario_bloqueado and usuario_funcionario

if (funcionario_ativo and horario_comercial) or (usuario_admin):
    print('acesso liberado')
else:
    print('acesso negado')

# está bem ilegível
# if (not usuario_bloqueado and usuario_funcionario and hora>8 and hora<18) or (usuario_admin):
#    print('acesso liberado')
# else:
#    print('acesso negado')

# outro arquivo
# para não ter de escrever essa condição de novo
horario_comercial = hora>8 and hora<18

if horario_comercial:
    print("dentro do horario comercial")

# usa função, para poder usar em outro arquivo
def dentro_horario_comercial (hora):
    return hora>8 and hora<18

if dentro_horario_comercial(hora):
    print("dentro do horario comercial")


# operadores de comparação
# ==, !=, >, <, <=, >=
nota1 = 10.0
nota2 = 5.5

# aluno foi melhor na primeira prova (nota1) ou na segunda prova (nota2)
if nota1>nota2:
    print('Aluno foi melhor na prova 1')
else:
    print('Aluno foi melhor na prova 2 ou teve mesma nota nas duas')

# ------------------------------
# -1 -2 0 1 2 3 4 5
# 4>    | -->  
# 4>=   |4-->


# operador is, is not
# operador identidade
# comparar se os objetos são os mesmos
# mesmo espaço de memória

a = [1,2,3]
b = [1,2,3]
# vai dar true pois são os mesmos valores
print (a == b) 

# vai dar false pois são variáveis diferentes
print (a is b)

# usado para verificar se um elemento existe em uma sequencia
# str, lista, tupla

opcoes = ('sim', 'nao', 'talvez')
opcao = input('digite uma opcao: ')
opcao = opcao.lower().strip()

if opcao in opcoes:
    print('opcao valida')
else:
    print('invalido')

# para não e nao, teria que verificar depois, logo
# seria melhor usar dicionario ate
opcoes = {
    'sim' : ['sim', 's', 'y', 'yes'],
    'nao' : ['nao', 'n', 'não']
}