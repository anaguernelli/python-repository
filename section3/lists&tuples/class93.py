''' strip - join'''

frase = 'Olha, só ,isso'

lista_palavras = frase.split(',')

lista = []

for i, frase in enumerate(lista_palavras):
    lista.append(lista_palavras[i].strip())

print('Split, append e strip:')
print(lista)
print(lista_palavras)

unifica_lista = '-'.join(lista)

print('\nJoin:')
print(unifica_lista)
