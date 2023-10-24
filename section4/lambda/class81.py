'''
Lambda

A função lambda é anônima e contém apenas uma linha, ou seja, 
tudo deve ser contido dentro de uma única expressão

'''

# lista = [1, 2, 3, 4]
# lista.sort(reverse=True)
# sorted(lista)

# Lista com dicionários - Como ordenar?

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


# def ordena(item):
#     print(item)
#     return item['nome']


# Apenas atribuímos À key a função ordena
# lista.sort(key=ordena)


# Agora, o mesmo usando a lambda
# lista.sort(key=lambda item: item['nome'])


# Usando a função sorted()

def exibe(lista):
    for items in lista:
        print(items)
    print('-'*45)


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibe(l1)
exibe(l2)
