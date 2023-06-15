# tuple é imutável, não te possibilita trocar os valores depois de definidos

# é possível transformar uma tupla em lista

nomes_tupla = 'oi', 'tudo', 'bem'
nomes = list(nomes_tupla)

# é possível transformar uma lista em tupla

nomes_lista = ['oi', 'tudo', 'bem']
nomes = tuple(nomes_lista)

print(nomes)

print(nomes[-1])
