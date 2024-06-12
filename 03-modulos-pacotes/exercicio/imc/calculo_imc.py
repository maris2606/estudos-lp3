from imc.classificacao import classificacoes
from math import pow

def imc(peso, altura):
    return round(peso / pow(altura, 2), 1)

def classificar(imc):
    for classe in classificacoes:
        if imc >= classificacoes[classe][0] and imc <= classificacoes[classe][1]:
            return classe

def peso_a_ganhar_ou_perder(peso, altura):
    imc_normal = 24.9
    peso_normal = imc_normal * pow(altura, 2)

    diferenca = peso - peso_normal

    if diferenca < 0:
        return f'você precisa ganhar {abs(round(diferenca, 1))} kg'
    else:
        return f'você precisa perder {round(diferenca, 1)} kg'
