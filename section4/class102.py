# Variáveis livre e nonlocal (locals, globals)

# def fora(x):
#     a = x

#     def dentro_da_funcao():
#         # retorna variavel que pode ser executada
#         # tanto fora quanto dentro da função
#         print(locals())
#         return a

#     return dentro_da_funcao


# dentro1 = fora(2)
# dentro2 = fora(33)

# print(dentro1())
# print(dentro2())


def concatene(valor_inicial):
    valor_final = valor_inicial

    def interna(valor_concatenado):
        # sendo valor_final uma free var,
        # devemos defini-la como nonlocal
        nonlocal valor_final
        valor_final += valor_concatenado

        return valor_final

    return interna


concatenando = concatene('oi')

print(concatenando(', ana'))
print(concatenando(', pedrin'))
