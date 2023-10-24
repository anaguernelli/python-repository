try:
    x = 6
    y = 0
    xy = x / y
except ZeroDivisionError:
    print('Erro: Divisão por zero')
except NameError:
    print('Erro: NameError')
except (TypeError, IndexError) as error:
    print('Erro: Erro de digitação + IndexError')
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)    # Nome do erro
except Exception:   # Não é boa prática apenas Exception
    print('Erro: Erro desconhecido')
