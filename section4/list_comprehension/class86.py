produto = {
    'nome': 'Caneta',
    'preco': 3.5,
    'categoria': 'escritorio',
}

dc = {
    chave: valor.upper()
    # Se o valor for do tipo str
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave == 'categoria'
}

print(dc)


set_comprehension = {i for i in range(10)}
# set_comprehension = set(range(5))

print(set_comprehension)