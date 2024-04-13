# Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
# O programa deve pedir ao usuário para votar várias vezes e, no final, 
# mostrar o número de votos de cada candidato e quem foi o vencedor

pessoas = int(input('quantas pessoas irão votar? '))

def votacao(pessoas):
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0

    i = 0
    while i < pessoas:
        voto = int(input('digite o número de seu candidato (1-João, 2-Ana, 3-Maria): '))

        match voto:
            case 1:
                candidato1 +=1
            case 2:
                candidato2 +=1
            case 3:
                candidato3 +=1
            case _:
                print('candidato inválido, digite novamente:')
                i-=1
        i+=1

    if candidato1>candidato2 and candidato1>candidato3:
        return ('João', candidato1, candidato2, candidato3)
    
    elif candidato2>candidato1 and candidato2>candidato3:
        return ('Ana', candidato1, candidato2, candidato3)
    
    elif candidato3>candidato1 and candidato3>candidato2:
        return ('Maria', candidato1, candidato2, candidato3)

    else:
        return ('Empate', candidato1, candidato2, candidato3)

resultado_votacao = votacao(pessoas) 

if resultado_votacao[0] == 'Empate':
    print('\nNão houve vencedor. Houve empate.')
else:
    print(f'\nO vencedor foi o candidato(a) {resultado_votacao[0]}')

print(f'\nnúmero de votos: \nJoão: {resultado_votacao[1]}\nAna: {resultado_votacao[2]}\nMaria: {resultado_votacao[3]}')


