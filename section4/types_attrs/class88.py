'''
Valores truthy e falsy, tipos mutáveis e imutáveis

Mutáveis (Falsy) -> [] {} set()

Imutáveis -> (), "", 0, 0.0, None, False, range(0, 10)
'''
lista = []
dicti = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def is_falsy(valor):
    return 'falsy' if not valor else 'truthy'


print(f'Testando - {is_falsy('Testando')}')
print(f'{lista} - {is_falsy(lista)}')
print(f'{dicti} - {is_falsy(dicti)}')
print(f'{conjunto} - {is_falsy(conjunto)}')
print(f'{tupla} - {is_falsy(tupla)}')
print(f'{string} - {is_falsy(string)}')
print(f'{inteiro} - {is_falsy(inteiro)}')
print(f'{flutuante} - {is_falsy(flutuante)}')
print(f'{nada} - {is_falsy(nada)}')
print(f'{falso} - {is_falsy(falso)}')
print(f'{intervalo} - {is_falsy(intervalo)}')
