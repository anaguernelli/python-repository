
# somente p números de ponto flutuantes extensos
# e queira ter maior precisão
import decimal

num1 = decimal.Decimal(0.1)
num2 = decimal.Decimal(0.7)
num3 = num1 + num2

# Arredondar números decimais

print(f'{num3}')
print(f'{num3:.2f}')
print(round(num3, 2))
