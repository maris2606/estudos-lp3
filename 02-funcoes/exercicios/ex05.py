# Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e 
# verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

texto = input('digite a palavra ou frase: ')

def verifica_palindromo(texto):
    texto_invertido = texto[::-1] # inverte o texto

    # socorram me subi no onibus em marrocos
    if texto.upper().replace(' ', '') == texto_invertido.upper().replace(' ', ''):
        return 'é palíndromo!'
    else:
        return 'não é palíndromo...'

print(verifica_palindromo(texto))