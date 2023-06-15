"""
alert: este é um código porcedural!!
"""
import random
import re
import sys

# gerando números aleatórios para CPF
digitos9 = ''

for i in range(9):
    digitos9 += str(random.randint(0, 9))
print(digitos9)

'''
 Usando expressão regular

entrada = input("Informe seu CPF [738.244.543.92]: ")
cpf_usuario = re.sub(
    # estamos fazendo uma substituição de tudo
    # que não for um número na string para ''
    r'[^0-9]',
    '',
    entrada
    )


is_digitos_sequenciais = entrada == entrada[0] * len(entrada)

if is_digitos_sequenciais:
    print("VocÊ enviou dados sequenciais")
    sys.exit()
'''

result1 = 0
regress1 = 10

for digito in digitos9:
    result1 += int(digito) * regress1
    regress1 -= 1

digito1 = (result1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

# if digitos > 9:
#     result = 0
# else:
#     result = digitos
digitos10 = digitos9 + str(digito1)
regress2 = 11
result2 = 0

for digito in digitos10:
    result2 += (int(digito) * regress2)
    regress2 -= 1

digito2 = (result2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
print(f"O primeiro dígito do CPF é {digito1} e o segundo é {digito2}")

cpf_gerado_calculo = f"{digitos9}{digito1}{digito2}"

print(cpf_gerado_calculo)
