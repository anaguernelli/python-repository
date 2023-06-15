'''
Higher Order Functions

Funções que podem receber e/ou retornar outras funções

'''


def saudar(msg, nome):
    return f'{msg}, {nome}!'


def executar(func, *args):
    return func(*args)


p = executar(saudar, 'Good', 'Ana')
print(p)
