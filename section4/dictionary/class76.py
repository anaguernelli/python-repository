person = {
    'nome': 'ana',
    'idade': 12,
    'endereco': [
        {'rua': 'Av. das Americas', 'numero': 1712},
    ],
}


# for i in person:
#     print(i, person[i])


person['sobrenome'] = 'Silva'
print(person['endereco'])

del person['sobrenome']
print(person)
print(person['nome'])

# Quando procurar uma chave inexistente em um dict,
# podemos tanto usar o try/except como get()

if person.get('sobrenome') is None:
    print('Nao existe')
else:
    print(person['sobrenome'])
