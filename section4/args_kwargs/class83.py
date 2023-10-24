# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a


pessoa = {
    'nome': 'Vex',
    'sobrenome': 'Vlala',
}

pessoa_data = {
    'idade': 12,
}

pessoas_completa = {**pessoa, **pessoa_data}
print(pessoas_completa)


a, b = pessoa.values()
(a1, a2), (b1, b2) = pessoa.items()


print(a, b)  # Vex Vlala
print(a1, a2)   # nome Vex
print(b1, b2)   # sobrenome Vlala

# O mesmo com o for

for nome, valor in pessoa.items():
    print(nome, valor)


def show_argumentos(*args, **kwargs):
    print(args, kwargs)

    for i, value in kwargs.items():
        print(i, value)


show_argumentos('ana', nome='anao')
print()
show_argumentos(**pessoas_completa)
