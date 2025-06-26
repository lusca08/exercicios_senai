# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------



dolar = float(input('digite a cotação do dólar: '))
valor_em_real = float(input('digite o valor em dólar a ser convertido em real: '))
valor_convertido = valor_em_real * dolar
print(f'O valor convertido em reais é: R$ {valor_convertido: }')





