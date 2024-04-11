# Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
# O programa deve pedir ao usuário para votar várias vezes e, no final, 
# mostrar o número de votos de cada candidato e quem foi o vencedor

candidato1 = 0
candidato2 = 0
candidato3 = 0

pessoas = int(input('quantas pessoas irão votar? '))
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

print(f'número de votos: \nJoão: {candidato1}\nAna: {candidato2}\nMaria: {candidato3}')

if candidato1>candidato2 and candidato1>candidato3:
    print(f'o vencedor é o João!')
elif candidato2>candidato1 and candidato2>candidato3:
    print(f'a vencedora é a Ana!')
else:
    print(f'a vencedora é a Maria!')

