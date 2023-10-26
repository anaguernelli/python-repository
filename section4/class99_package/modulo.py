'''
Quando for importado *
__all__ = [
    'uma_variavel',
    'package_multiplica',
]

obs: as importações do package têm de ser como
se estivéssemos no arquivo class99
'''
# from class99_package.modulo_b import cumprimenta
from .modulo_b import cumprimenta


uma_variavel = 'Variavel'


def package_multiplica(x, y):
    return x * y


cumprimenta()
