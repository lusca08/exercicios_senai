continuar = 's'
while continuar == 's':
    print(f'{"-"*30}')
    print(f'{" Calculadora ":^30}')
    print(f'{"-"*30}')

    print('| 1 - Soma        |')
    print('| 2 - Subtração   |')
    print('| 3 - Multiplicação|')
    print('| 4 - Divisão     |')
    print(f'{"-"*30}')

    escolha = int(input('| Escolha uma das opções: '))
    n1 = float(input('| Digite o primeiro número: '))
    n2 = float(input('| Digite o segundo número: '))

    if escolha == 1:
        print(f'| O resultado é: {n1+n2}')
    elif escolha == 2:
        print(f'| O resultado é: {n1-n2}')
    elif escolha == 3:
        print(f'| O resultado é: {n1*n2}')
    elif escolha == 4:
        print(f'| O resultado é: {n1/n2}')
    else:
        print('| ERRO. Escolha uma opção válida.')

    continuar = input('| Deseja continuar? (s/n) ')
    print()

print('--FIM DO PROGRAMA--')
