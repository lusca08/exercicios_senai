nome = input('Qual é seu nome? ')
idade = float(input('QUal sua idade? '))
if idade  >= 18:
    print('Maior de idade')
    
    carteira = int(input('você possui carteira de motorista? 1-sim 2-não'))
    if carteira == 1:
        print('pode dirigir!')
    else:
        print('não pode dirigir')

    
else:
    print('Menor de idade')