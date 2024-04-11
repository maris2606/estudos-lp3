# Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
# converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

# https://www.ifsp.edu.br/images/pdf/Seletivo1_2018/Processo_seletivo_2/Anexo-I---Tabela-de-equivalncia-entre-conceitos-e-notas-numricas.pdf
# A = 10
# B = 7.5
# c = 5
# D = 2
# F = 0

pontuacao = int(input('insira uma pontuação de 0 a 100: '))/10

if pontuacao <= 10 and pontuacao>=0:
    if pontuacao == 10:
        print('Nota: A')
    elif pontuacao >= 7.5:
        print('Nota: B')
    elif pontuacao >= 5:
        print('Nota: C')
    elif pontuacao >= 2:
        print('Nota: D')
    else:
        print('Nota: F')
else:
    print('nota inválida')
