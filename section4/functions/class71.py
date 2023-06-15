# *args - argumentos não nomeados
# empacotamento e desempacotamento

def soma(*args):
    tot = 0
    for numero in args:
        tot += numero
    
    return tot


numeros = 1, 2, 3, 4, 5, 10
# Pois nossa func aceita só desempacotamento
segunda_soma = soma(*numeros)
print(segunda_soma)

# E o sum() permite somente até 2 argumentos
print(sum(numeros))
