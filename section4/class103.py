'''
Funções decoradoras ou decorators

Funções que decoram outras funções para:
Adicionar | Remover | Restringir | Alterar

'''
# Função decorada


def create_func(func):
    def intern(*args, **kwargs):
        print('It will be decorated')
        for arg in args:
            is_string(arg)

        result = func(*args, **kwargs)
        print('Now you are decorated')

        return result

    return intern


def inverse_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Must be a string')


inverse_string_check_param = create_func(inverse_string)
inverse = inverse_string_check_param('Aninhao')
print(inverse)
