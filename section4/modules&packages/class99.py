'''
    Introdução aos packages
    Este arquivo de entrada class99 é o __main__
    E pode importar qualquer coisa desse main
'''

# from sys import path
# from class99_package.modulo import package_multiplica   # Forma correta
# from class99_package import modulo  # modulo.package_multiplica()
# from class99_package.modulo import *  # má prática!

# print(*path, sep='\n')
# print(package_multiplica(1, 2))


# Com o * tenho acesso à variavel, mas não tenho acesso
# a outras coisas caso eu não explane no __all__

# from class99_package.modulo import package_multiplica, cumprimenta

# cumprimenta()
# print(package_multiplica(3, 5))

from class99_package import package_multiplica

print(class99_package.duplica(3))
