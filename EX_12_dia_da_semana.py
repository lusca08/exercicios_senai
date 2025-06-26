# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dia = float(input('digite um número: '))
if dia == 1:
    print('domingo')
elif dia == 2:
    print('segunda-feira')
elif dia == 3:
    print('terça-feira')
elif dia == 4:
    print('quarta-feira')
elif dia == 5:
    print('quinta-feira')
elif dia == 6:
    print('sexta-feira')
elif dia == 7:
    print('sábado')
else:      
    print('este número é inválido.')