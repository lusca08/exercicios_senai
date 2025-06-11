# IMC fórmula : peso / (altura X altura)


altura = float(input('digite sua altura:'))
peso = float(input('digite seu peso:'))
imc = peso / (altura ** 2)

resultado = round(imc, 2)

print(resultado)
