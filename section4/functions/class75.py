'''
Make functions that can duplicate, triplicate and quadruplicate
the number received as a parameter
'''


def criar_multiplicador(multiplicador):
    def multiplicacao(numero):
        return numero * multiplicador
    return multiplicacao

# Importante: para que a função dentro da função funcione, deve retorná-la!!!


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(triplicar(2))

print(f'O resultado da multiplicação escolhida é {quadriplicar(2)}')
