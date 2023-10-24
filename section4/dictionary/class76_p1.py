'''
    Métodos úteis do dict em Python
    len - quantas chaves
    keys - iterável com as chaves
    values - iterável com os valores
    item - iterável com chaves e valores
    setdefault - adiciona valor se chave não existe
    copy - retorna uma copia rasa (shallow copy)

'''

person = {
    'nome': 'Pedro',
    'sobrenome': 'Pali',
    'idade': 20,
}

print(len(person))  # 3

# Não esqueça que pode usar um for para apresentar chaves e valores

print(person.keys())    # dict_keys(['nome', 'sobrenome', 'idade'])
print(list(person.keys()))    # ['nome', 'sobrenome', 'idade']
print(list(person.values()))    # ['Pedro', 'Pali', 20]
print(list(person.items()))  # [('nome', 'Pedro'), ('sobrenome', 'Pali'),('idade', 20)]

for i in person:
    print(person)    # Pedro  Pali  20

# Similar ao get(), setdefault( implementa valor padrão caso valor não exista)

print(person.setdefault('age', 'Valor padrão'))
