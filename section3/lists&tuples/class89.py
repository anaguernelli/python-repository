'''
enumerate - enumera iteráveis (índices!)
'''

lista = ['maria', 'ana', 'pedro']
lista.append('Joao')

lista_enumerate = enumerate(lista)
print(next(lista_enumerate))
# precisamos dar o next(), dando o indice 0 e seu valor em tupla
# pois enumerate é uma tupla
# print(lista_enumerate) vai dar o endereço de memória da lista

# o for atua como o next,
# mas listando todos os itens ao invés de um:

for item in lista_enumerate:
    print(item)

# podemos apenas converter a lista para list

lista_enumerate = list(enumerate(lista))

# or

for indice, valor in enumerate(lista):
    print(indice, valor)

# voce pode chamar uma lista inteira desta forma tbm
# e sendo automaticamente espaçadas

print(*lista)
print(*lista, sep='\n')
print(*lista, end='--')
