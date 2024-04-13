# Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input('digite um número: '))

def tabuada (numero): # retorna lista com as multiplicações e resultados
    return [(f'{numero} * {i} = {numero * i}') for i in range(1, 11)]

print('Tabuada:')
for mult in tabuada(numero):
    print(mult)