import sys

''' Generator expression, Iterables e
    iterators (entrega valor por vez)
    Generator normalmente são funções que sabem pausar
    e o iterator trabalha entregando valor por vez
'''

iterable = ['Tenho', 'um', '__iter__']
iterator = iter(iterable)  # tem o __iter__ e o __next__

# Uma lista com muitos dados na memória (pode gerar problemas)
lista = [numero for numero in range(50000)]

# Aqui um generator expression
generator = (numero for numero in range(5))

'''
    A medida que aumento os valores na lista, + aumenta os bits na memória
    o generator apenas entrega um valor por vez, não guardando na memória
    Por conta disso, não se pode acessar o generator através de índices, len..
'''

print(sys.getsizeof(lista))     # 444376
print(sys.getsizeof(generator))     # 192
# print(next(generator))

# for n in generator:
#     print(n)
