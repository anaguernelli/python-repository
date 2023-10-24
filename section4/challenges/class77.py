# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acerto = 0

for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}')

    opcoes = pergunta['Opções']
    for num, valor in enumerate(opcoes):
        print(f'{num}) {valor}')

    escolha = input('Escolha uma opção: ')

    acerto = False
    escolha_converte_int = None
    qtd_ops = len(perguntas)

    if escolha.isdigit():
        # Aqui deixa de ser None!
        escolha_converte_int = int(escolha)

    if escolha_converte_int is not None:
        if escolha_converte_int >= 0 and escolha_converte_int <= qtd_ops:
            if opcoes[escolha_converte_int] == pergunta['Resposta']:
                acerto = True

    if acerto:
        qtd_acerto += 1
        print('Acertou :D')
    else:
        print('Errou D:')

print(f'Você acertou {qtd_acerto} de {len(perguntas)} perguntas')


# Tentativa 1 (not clean)

# cont = 0
# acertos = 0

# while True:
#     print(f'Pergunta: {perguntas[0]['Pergunta']}')
#     print('Opções:')

#     for i, valor in enumerate(perguntas[0]['Opções']):
#         print(f'{i}) {valor}')

#     op = input('Escolha uma opção: ')
#     if op == 2:
#         acertos += 1
#         print('Parabéns! :D')
#     else:
#         print('Errou :(')
#         continue

#     print(f'Pergunta: {perguntas[1]['Pergunta']}')
#     print('Opções:')

#     for i, valor in enumerate(perguntas[1]['Opções']):
#         print(f'{i}) {valor}')

#     op = input('Escolha uma opção: ')
#     escolha_int = None

#     if op.isdigit():
#         # Sendo um dígito, será convertido para int
#         escolha_int = int(op)
#         if op == 0:
#             acertos += 1
#             print('Parabéns! :D')
#         else:
#             print('Errou :(')
#             continue

#     print(f'Pergunta: {perguntas[2]['Pergunta']}')
#     print('Opções:')

#     for i, valor in enumerate(perguntas[2]['Opções']):
#         print(f'{i}) {valor}')

#     op = input('Escolha uma opção: ')
#     if op == 1:
#         acertos += 1
#         print('Parabéns! :D')
#     else:
#         print('Errou :(')
#         break

# print(f'Voce acertou no total {acertos} perguntas de 3')
