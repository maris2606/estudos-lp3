# for, while, break, continue

# operador in
# para cada letra em string 'Python'
for letra in 'Python':
    print(letra)

itens = ['banana', 'arroz', 'limão']
for item in itens:
    print(item)

# normalmete não se sabe quantos valores tem
# por isso precisa do for


# iterar parte da lista
for i in range(5):
    print(i)

for i in range(0, 11, 2):
    print(i)

# botar 100 números numa lista
lista = list(range(101))

#tipo
print(type(10))

#tamanho de sequência
print(len([0,1,2,4,5,6,7,8,9]))

# só usar range em casos específicos
# não fazer assim:
# for i in range(len([lista/array/string])):
#     print(i)


#while
contador = 0
while contador <= 5:
    print(contador)
    contador += 1

print('-------------------')

# break
# parar totalmente a iteração
# encontre o primeiro número par
numeros = [1, 3, 5, 7, 8, 2]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)

print('-------------------')

# continue
numeros = [-3, -1, 6, 0, -2]

for numero in numeros:
    if numero <= 0:
        continue # para a iteração, não vai para as linhas de baixo
    print(numero)


# compreensao de lista
# forma concisa de criar lista em python
numeros = [2, 3, 4, 5, 6]
quadrados = []

# sem compreensão de listas
for numero in numeros:
    quadrados.append(numero ** 2)

print(numeros)
print(quadrados)

# com compreensão de listas
#   faça numero ao quadrado para cada numero em numeros
quadrados = [numero ** 2 for numero in numeros]

palavra = 'ola mundo'
letras = [letra.upper() for letra in palavra]
print(letras)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# e se não for só o mapeamento
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)