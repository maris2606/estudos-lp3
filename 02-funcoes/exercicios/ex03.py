# Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase

frase = input('digite uma frase: ')
vogais = ['A', 'I', 'U', 'E' ,'O']
numero_vogais = 0
numero_consoantes = 0

for letra in frase.upper():
    # não funcionou o strip() por algum motivo
    if letra in vogais:
        numero_vogais +=1
    elif not letra.isspace():
        numero_consoantes += 1

print(f'o número de consoantes na frase: {frase} é {numero_consoantes},\n enquanto o número de vogais é {numero_vogais}.')