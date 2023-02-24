# todo parâmetro que vier DEPOIS de um parâmetro padrão,
# ele obrigatoriamente terá de ser padrão

def soma(x, y=None, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} =', x + y + z)
    else:
        print(f'{x=} {y=} =', x + y)

soma(1, 2)
soma(1, 2, 3)
soma(1)



