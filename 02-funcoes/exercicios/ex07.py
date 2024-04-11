# Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. 
# O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra.
# O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

palavra_original = 'latorre' # guarda a palavra original para exibir ao final do jogo
palavra = [letra for letra in palavra_original]
forca = ['_','_','_','_','_','_','_']
adivinhadas = []
vidas = 3 # como não era especificado, coloquei 3 vidas

# não queria a formatação normal de array pq tava muito poluido...
def exibe(caracteres, deco1= '', deco2=''): 
    print(deco1, end=' ')

    for letra in caracteres:
        print(letra, end=' ')

    print(deco2, end=' ')
    print('\n')

def entrada():
    letra = input('adivinhe uma letra: ').lower() # coloca em minúsculo para garantir
    if len(letra)==1 and letra.isalpha(): # só pode uma letra por vez, e deve ser letra
        return letra
    else:
        return 0

# retorna 0 se errar, 1 se acertar, 2 se precisar digitar de novo, 3 se for repetida
def jogo_da_forca(): 
    print('\n+-----------------------------------------------+')
    exibe(forca)

    adivinhacao = entrada()

    if adivinhacao == 0:
        # vai mandar digitar de novo.
        return 2

    if adivinhacao in adivinhadas:
        # já foi adivinhada, perde ponto.
        return 3
    
    elif adivinhacao not in adivinhadas and adivinhacao in palavra:
        # se não foi adivinhada e existe na palavra
        adivinhadas.append(adivinhacao)
        print('\n- adivinhadas: ')
        exibe(adivinhadas,'[',']') # mostra quais letras já foram.

        # adiciona na forca
        for letra in palavra:
            if letra == adivinhacao:
                forca[palavra.index(adivinhacao)] = adivinhacao
                palavra[palavra.index(adivinhacao)] = ''
                
        exibe(forca)
        return 1

    elif adivinhacao not in adivinhadas and adivinhacao not in palavra:
        # não foi adivinhada e está incorreto
        adivinhadas.append(adivinhacao)
        print('\n- adivinhadas: ')
        exibe(adivinhadas,'[',']')
        # só adiciona nas já adivinhadas
                
        exibe(forca)
        return 0


def pontuar (vidas):
    while vidas: # enquanto vidas for diferente de 0
        if '_' in forca:
            status = jogo_da_forca()

            match status: # testa o status do jogo
                case 0:
                    print('errou!')
                    vidas -= 1
                case 1:
                    print('acertou!')
                case 3:
                    print('repetida! perde uma vida.')
                    vidas -= 1
                case _:
                    print('caractere inválido,')
                    print('digite novamente: ')
        elif '_' not in forca:
            return True # adivinhou toda a palavra
        else:
            return False # perdeu


venceu = pontuar(vidas)

if venceu:
    print('\nParabens você conseguiu adivinhar a palavra!')
    exibe(deco1='[', caracteres=palavra_original, deco2=']')
else: 
    print('\nque pena, não foi dessa vez... a palavra era:')
    exibe(deco1='[', caracteres=palavra_original, deco2=']')
