# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


dias= float(input('quantidade de dias de uso: '))
km= float(input('quantidade de km percorrido: '))

valor_dias=dias*60
valor_km=km*0.15
valor_total = valor_dias+valor_km

print(f'você andou {km} por {dias} o valor que você tem que pagar é {valor_total}')