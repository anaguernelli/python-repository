# raise - levantando exceções


def no_zero(d):
    if d == 0:
        raise ZeroDivisionError('Não é possível dividir por zero.')

    return True


def deve_ser_int_float(n, d):
    tipo_n = type(n)
    tipo_d = type(d)

    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" não é um número.'
            f'\n"{tipo_n.__name__}" foi enviado.'
        )

    if not isinstance(d, (float, int)):
        raise TypeError(
            f'"{d}" não é um número.'
            f'\n"{tipo_d.__name__}" foi enviado.'
        )

    return True


def dividir(n, d):
    deve_ser_int_float(n, d)
    no_zero(d)

    return n / d


print(dividir('jjj', 'jsjds'))
