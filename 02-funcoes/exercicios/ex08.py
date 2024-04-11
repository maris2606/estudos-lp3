# Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e 
# retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. 
# Depois, teste a função com diferentes textos fornecidos pelo usuário.

frase = input('Digite sua frase: ')

def montar_dicionario(frase):
    palavras = ''

    for letra in frase: # retira qualquer caractere especial ou numero.
        if letra.isalpha() or letra == ' ':
            palavras += letra.lower()
    palavras = palavras.split() # separa as palavras

    dicionario = {}

    for palavra in palavras: # para cada palavra
        if palavra in dicionario: # se já existe, soma 1 a quantidade
            numero = dicionario.get(palavra)
            dicionario.update({palavra: numero + 1})
        else: # senão, cria uma chave com um valor incial.
            numero = 1
            dicionario.update({palavra: numero})

    return dicionario

dicionario = montar_dicionario(frase)
print(dicionario)