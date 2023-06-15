# "desempacotamento"
# isto [] ainda é uma lista, uma tu
name0, *_ = ['ana', 'tae', 'jk', 'something']
print(name0, _)

# name1 terá valor 'ana', e _ com * terá do indice 1 ao 3
# muitos desenvolvedores utilizam o _ quando
# não querem utilizar de uma variável

# _, _, primeiro, *_ = ['ana', 'tae', 'jk', 'something']
# print(primeiro)