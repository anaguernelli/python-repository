# List comprehension com mais de um for

lista = []

# Normal
for x in range(2):
    for  y in range(2):
        lista.append((x, y))


# List Comprehension
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# List Comprehension dentro de  list comprehension
lista = [
    [(x, letra) for letra in 'Pedro']
    for x in range(3)
]

print(lista)
