# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
nome = input('Digite seu nome: ')
n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
n3 = float(input('Nota da terceira prova: '))
soma = n1 + n2 + n3
media = soma / 3
print('')
print(f'| {"-"*30}| ')
print(f'| SISTEMA DE PROVAS')
print(f'| {"-"*30} |')
print('| Nota da primeira prova: ', n1)
print('| Nota da segunda prova: ', n2)
print('| Nota da terceira prova: ', n3)
print(f'| {"-"*30} |')
print('| Aluno: ', nome)
print('| Média: ', media )
if media <= 6:
    print('Aluno reprovado')
else:
    print('Aluno Aprovado')
print(f'| {"-"*30} |')

