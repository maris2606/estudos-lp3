# Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
# Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

numero = 5
acertou = False

def dica (palpite):
    if (palpite > numero):
        return 'o palpite está alto'
    elif (palpite < numero):
        return 'o palpite está baixo'
    else:
        return 'acertou!'
    

palpite = int(input("Adivinhe um número: "))

if palpite > 0 and palpite< 100:
    print(dica(palpite))

    while not dica(palpite) == 'acertou!':
        palpite = int(input("Adivinhe um número: "))
        if not(palpite > 0 and palpite< 100): break
        print(dica(palpite))
        
