from collections import Counter

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def duplicados(lista_int):
    check_num = set()
    duplicado = -1

    for numero in lista_int:
        if numero in check_num:
            duplicado = numero
            break

        # Se não passar pra condição, vai adicionando numero ao set
        check_num.add(numero)

    return duplicado


for lista in lista_de_listas_de_inteiros:
    print(lista, duplicados(lista))


# Tentativa 1

# for i in range(len(lista_de_listas_de_inteiros)):
#     lista_rep = Counter(lista_de_listas_de_inteiros[i])

#     if lista_rep >= 2:
#         print(lista_rep)
