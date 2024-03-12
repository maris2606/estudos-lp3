# if
idade = 20

if idade >= 18:
    print('Maior de idade')
    # precisa estar identado com 2 ou 4 espaços
    # o bloo de código deve estar com o mesmo espaçamento

# if/else
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# if/elif/else
# criança 1 - 12
# adolescente 13 - 17
# adulto 18 - 59
# idoso 60+

if idade <= 12:
    print ('crianca')
elif idade <= 17:
    print ('adolescente')
elif idade <= 59:
    print ('adulto')
else:
    print ('idoso')

# exemplo de if aninhado
email = 'admin@email.com'
senha = '123'

# código muito aninhado fica ilegível.
# if email == 'admin@email.com':
#     if senha == '123':
#         print ('acesso permitido')
#     else:
#         print ('invalido')
# else:
#     print('invalido')

if email == 'admin@email.com' and senha == '123':
    print ('acesso permitido')
else:
    print('invalido')


# entrada numero
# 1 - domingo
# 2 - segunda
# 3 - terca
# 4 - quarta
# 5 - quinta
# 6 - sexta
# 7 - sabado

dia = 4

dias = {
    1 : 'domingo',
    2 : 'segunda',
    3 : 'terca',
    4 : 'quarta',
    5 : 'quinta',
    6 : 'sexta',
    7 : 'sabado'
}

if dia in dias:
    print(dias[dia])

