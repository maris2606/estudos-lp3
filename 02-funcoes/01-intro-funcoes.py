# Funções
# mini programa que tem entrada, processamento e saída

# declaração
# def nome_da_funcao (parametro1, parametro2):
#     return valor

# funções sem retorno e sem parametro
def imprimir_saudacao():
    print('Bom dia Maria')
# sempre que tem : -> é o código do bloco - determinado pela identação

# função sem retorno e com parametros
def imprimir_nome(nome):
    print(f"Nome: {nome}")

# parametro vs. argumento
# parametro é a referencia definida na assinatura da função 
# pode acessar em qualquer lugar da função
# def imprimir_nome(nome): <- nome
# argumento é a referencia enviada/ passada para um parametro
# literal ou referencia (de uma variável), ou a chamada de uma função
# imprimir_nome('latorre') <- 'latorre'

# função com retorno sem parametros
def gerar_saudacao():
    return 'bom dia'
# return não é obrigatório

# função com retorno e com parametros
def gerar_saudacao_parametros(nome):
    return f'bom dia {nome}'

# chamada
# neste exemplo já está declarada - nativa
print('Olá') 
# a função só pode ser chamada depois da declaração
imprimir_saudacao()
imprimir_saudacao()

# argumento é a referencia enviada/ passada para um parametro
imprimir_nome('latorre')
# devemos evitar programar funções que já existem
saudacao =  gerar_saudacao()
print(saudacao)

print(gerar_saudacao())

# não tem polimorfismo nesse sentido aqui, ele acaba sobrescrevendo o anterior
# so tem sobrescrita de métodos herdados
# overload - com assinaturas diferentes NÃO EXISTE EM PYTHON
saudacao_jose =  gerar_saudacao_parametros('jose')
print(saudacao_jose)

print( gerar_saudacao_parametros('jose') )

# return        params
#   0             0
#   0             1
#   1             0
#   1             1     (melhor caso)
# por que ele prefere ter param e return?
# imprimir a saudação
# bom dia NOME (dinamico) - elimina o primeiro e o terceiro
# segundo
def imprimir_saudacao(nome):
    print (f'bom dia {nome}') 

# ultimo (melhor)
# funcao pura -> não tem efeito colateral e nem acesso a estado global

# dividiu o problema em 2
# gerar saudação - puro
# imprimir
def imprimir_saudacao(nome):
    return f'bom dia {nome}' 
# melhor pq nem sempre queremos imprimir, 
# as vezes precisamos mandar no email, enviar, colocar num arquivo, salvar, etc.

# calcule as medias das notas de varios alunos
# entrada - [[10, 6],[7, 8],[6, 9]]
# calcule e imprima
# calcular_media- lista de notas - media
# calcular_medias - lista de lista de notas - listas de médias
# imprimir a lista de média
notas_alunos = [
    [10, 6],
    [7, 8],
    [6, 9]
]

def calcular_media(notas):
    return sum(notas) / len(notas)

def calcular_medias(notas_alunos):
    # lista de médias calculadas para cada cjt de notas de alunos
    return [calcular_media(notas) for notas in notas_alunos]

# forma procedural
def calcular_medias(notas_alunos):
    medias = []
    for notas in notas_alunos:
        medias.append(calcular_media(notas))
    return medias

print(calcular_medias(notas_alunos))
# ajuda a criar testes para ver as coisas separadamente

# evitar colocar coaisas que só são utilizáveis em um contexto
# tipo prints e inputs

# Argumentos nomeados - não precisar seguir a ordem de parametros definida na função
def nova_saudacao(nome, saudacao):
    return f'{saudacao} -{nome}'

print(nova_saudacao('joao', 'boa tarde'))
print(nova_saudacao('maris', saudacao='bom dia'))
print(nova_saudacao(nome='luciana', saudacao='oii jossana bom dia tudo beemm?'))
print(nova_saudacao(saudacao='boa noite', nome='jossana'))

# se for nomear um, nomeia todos
# mas se for nomear só o último, tudo bem
# ex.
print ('olá', 'mundo', sep='-')


# valores padrão para parametros
# pode simular chamar função com mesmo nome e params diferentes (overload)

def obter_saudacao(nome, saudacao='bom dia'):
    return f'{saudacao} -{nome}'

print(obter_saudacao('pedro')) # pode mandar um argumento só

# equivale a 
# def nova_saudacao(nome, saudacao):
#     return f'{saudacao} -{nome}'
# e
# def nova_saudacao(nome, saudacao):
#     return f'bom dia -{nome}'

# *args (Non-KeyWord Arguments)
def calcular_media2 (notas): 
    return sum(notas) / len(notas)

calcular_media2( [10, 4.0, 5, 9] ) # lista
calcular_media2( (10, 4.0, 5, 9) ) # tupla

# e se for sem lista ou tupla??
# não sabe qts argumentos vem, igual no print
def calcular_media2 (*notas): 
    return sum(notas) / len(notas)
# por baixo dos panos, diz que pode passar quantos argumentos quiser
# e o python os tranforma em tupla.

print( calcular_media2(10, 4.0, 5, 9) )
