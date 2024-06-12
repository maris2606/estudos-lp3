# Crie um programa que recebe como entrada o comprimento, 
# altura e a largura de um aquário e calcule as seguintes informações.

# - O volume do aquário em litros;
# - A potência do termostato necessária para manter 
#   a temperatura adequada dentro do aquário;
# - A quantidade em litros de filtragem por hora necessária 
#   para manter a qualidade da água.

# - Volume é dado por (comprimento * altura * largura) / 1000
# - A potência do termostato depende do tamanho do aquário e da
#   temperatura ambiente. Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
# - A quantidade de filtragem por hora deve ser no mínimo 2 a 3 
#   vezes o volume do aquário.
from modulo_ex1 import volume, potencia, filtragem_hora

comprimento = float(input("digite o comprimento: "))
altura = float(input("digite a altura: "))
largura = float(input("digite a largura: "))

volume_aquario = volume(comprimento, altura, largura)

print(f'volume: {volume_aquario}')

temp_ambiente = float(input("digite a temperatura ambiente: "))
temp_desejada = float(input("digite a temperatura desejada: "))
print(f"potencia: {potencia(volume_aquario, temp_desejada, temp_ambiente)}")
print(f"filtragem por hora: {filtragem_hora(volume_aquario)}")

