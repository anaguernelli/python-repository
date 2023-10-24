import pprint

'''
    List Comprehension é uma forma rápida
    de criar listas a partir de iteráveis


    Para que o 'for' funcione, precisamos dizer antes
    dizer o que queremos que seja incluído na repetição
    E podemos ainda usar uma lógica -> numero * 2
'''

lista = [numero for numero in range(5)]
# print(lista)


def elegant_print(x):
    pprint.pprint(x, sort_dicts=False, width=20)


# Mapeamento de dados em list comprehension
# *Transformar dado ou não e jogando para uma outra lista
# Aqui, de produtos para novos_produtos

produtos = [
    {'nome': 'Vex', 'preco': 16, },
    {'nome': 'Caneta', 'preco': 12, },
]

novos_produtos = [
    # {'nome': produto['nome'], 'preco': produto['preco']}
    {**produto, 'preco': produto['preco'] + 1.05}
    if produto['preco'] > 12 else {**produto}
    for produto in produtos
]

print(*novos_produtos)

elegant_print(novos_produtos)
