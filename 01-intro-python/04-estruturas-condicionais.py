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

# operador ternário
idade = 20

# sera maior ou menor de idade dependendo da idade
# if idade>= 18:
#     status = "maior de idade"
# else
#     status = "menor de idade" 

status = "maior de idade" if idade >= 18 else "menor de idade"

# match case
# python 3.10
# melhor que o switch case

dia = 3

match dia:
    case 1:
        print('domingo')    
    case 2:
        print('segunda')    
    case 3:
        print('terca')   
    case 4:
        print('quarta')    
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sabado')
    case _:
        print('invalido')

# imprimir
# 1 e 7 - fim de semana
# 2 3 4 5 6 - dia útil
match dia :
    case 1 | 7:
        print('fim de semana')
    case 2|3|4|5|6:
        print('dia útil')
    case _:
        print('dia inválido')
