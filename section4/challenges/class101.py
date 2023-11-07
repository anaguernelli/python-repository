# Adiando execuções


def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    # Closure, ou seja, uma forma de "guardarmos" na memória
    # a execução dessa função, para então executarmos o 'x' e o 'y'
    def closure_interna(y):
        return funcao(x, y)

    return closure_interna


# Criar um função que sempre soma por 5,
# o numero que for passado vai ser somado com 5

soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(2))

# Criar uma funçao que sempre multiplica por 10

multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(5))
