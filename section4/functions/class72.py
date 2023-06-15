def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero

        if numero == 0:
            print("0 não multiplica")
            return 0
    print(total)
    return total


multiplica(0, 2, 8, 44)


def parImpar(*args):
    for numero in args:
        if numero % 2 == 0:
            print("Par")
        else:
            print("Impar")


parImpar(3, 6)
