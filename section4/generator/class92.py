# Yield from - no generator


def gen1():
    yield 1
    yield 2
    yield 3


def gen_continua(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6


# Passando uma função como parametro
g = gen_continua(gen1)

for n in g:
    print(n)
