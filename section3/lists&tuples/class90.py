'''
lista de compras
user pode inserir, apagar e listar valores a lista
nao permita que o programa quebre por índices inexistentes
'''
import os

compras = ['Nada', 'oi']

while True:
    print('\nSelecione uma opção: ')
    escolhas = input('[I]nserir [A]pagar [L]istar: ').upper()[0]

    if escolhas == 'I':
        os.system('cls')
        inserir = input('O que deseja inserir a lista?\n').strip()
        compras.append(inserir)
        print(compras, f'{inserir} foi adicionado\n')

    elif escolhas == 'A':
        os.system('cls')
        apagar = int(input('Qual índice deseja apagar da lista?\n'))

        try:
            del compras[apagar]

        except ValueError:
            print('Por favor, digite um número')

        except IndexError:
            print('Índice inexistente, tente novamente\n')

        except Exception:
            print('Erro desconhecido')

    elif escolhas == 'L':
        os.system('cls')
        if len(compras) == 0:
            print('Nada a listar')
        for i, item in enumerate(compras):
            print(i, item)

    else:
        print('Por favor, escolha uma opção')

print('Programa finalizado!')
