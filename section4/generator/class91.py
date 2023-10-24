'''
    Generator function
    generator = (n for n in range(100000))
    Uma função que pausar ao invés de dar um break
'''


# def generator(numero=0):
#     yield 1   # Pausar
#     print('Mais um?')
#     yield 2
#     print('More?')
#     yield 5


def generator(numero=0, maximum=10):
    while True:
        yield numero
        numero += 1

        # Para que não se repita infinitamente, criaremos:
        if numero > maximum:
            return  # Aqui seria como um break


# gerar = generator(numero=0)
gerar = generator(maximum=19)

for i in gerar:
    print(i)
