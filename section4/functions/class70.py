x = 1


def escopo():

    x = 10

    def outra_func():

        x = 11
        y = 2
        print(x, y)

    outra_func()
    # Pega o x de seu próprio escopo(), outra_func() não altera
    print(x)


print(x)
escopo()
print(x)