# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome = input('Nome: ')
idade = input('idade: ')
email = input('email: ')
senha = input('senha: ')

print(f'| {"-"*30} |')
print(f'| {"-"*10} CADASTRO {10*'-'} |')
print(f'| {"-"*30} |')
print('| nome: ', nome)
print('| idade: ', idade)
print('| email: ', email)
print('| senha: ', senha)
print('')
print(f'| {"-"*30} |')
print(f'| {"-"*5} USUÁRIO CADASTRADO {5*'-'} |')
print('| Seja bem vindo(a)', nome )
print('|email: ', email)
print(f'| {"-"*30} |')