def executar(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplica(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


duplica = cria_multiplica(2)

print(
    executar(
        lambda x, y: x + y,
        2, 3
    ),
    executar(soma),
    soma(2, 3)
)
