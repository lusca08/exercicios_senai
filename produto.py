produto = input('nome do produto: ')
preço = float(input('informe o preço: '))
porcentagem = float(input('digite a porcentagem do valor do desconto:' ))

preço = porcentagem * (porcentagem / 100)
valor_novo = preço - porcentagem

print (f'O {produto} com {porcentagem} de desconto custará:R$ {valor_novo}')

