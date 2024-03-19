# crie um programa em python que recebe como entrada o valor de uma compra e apresenta como saída o valor final com desconto aplicado com base nas seguintes regras:
# compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
# compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
# compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
# compras iguais ou superiores a R$ 500,00 - 15% de desconto

compra = float(input('Digite o valor de sua compra:'))
desconto = 0
descontado = 0

if (compra >= 10.00) and (compra <= 99.99):
    desconto = 0.05
    descontado = compra - (compra * desconto)

elif (compra >= 100.00) and (compra <= 499.99):
    desconto = 0.10
    descontado = compra - (compra * desconto)

elif (compra >= 500.00):
    desconto = 0.15
    descontado = compra - (compra * desconto)
else:
    descontado = compra
    
print('o valor da compra com desconto de', desconto * 100,'% é:', descontado)