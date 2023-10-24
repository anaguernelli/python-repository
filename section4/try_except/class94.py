# try, except, else, finally
# finally sempre será executado

try:
    print('Abrindo arquivo...')
    8/0
except ZeroDivisionError:
    print('Dividiu zero')
else:
    print('Executado com sucesso')
finally:
    print('Fechando arquivo...')
