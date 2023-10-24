# isinstance() -> saber tipo do objeto

lista = [
    1, 7, 'Ana', [1,  2], {3, 4}, {'nome': 'sobrenome'}
]

for i in lista:
    if isinstance(i, set):
        i.add('SET')
        print(i, isinstance(i, set))

    elif isinstance(i, (int, float)):
        print('NUMBER', i)

    else:
        print('OUTRO')
