'''
    Sets em Python são conjuntos de dados mutáveis, porém aceitam
    apenas valores imutáveis (Não aceita listas dentro, tuplas sim etc)
    como valor interno e eliminam valores duplicados.
    + Não tem indexes
    + São iteráveis


    Dica: Caso queira remover valores duplicados de uma lista, pode
    convertê-la para set e depois para uma lista novamente

'''

# Criando set
set1 = set()
set2 = {'Ana', 1, 2, 2, 2}  # {1, 2, 'Ana'}

# Métodos úteis:
# add, update, clear, discard

set1.add(3)
set1.update(('Olá mundo', 12, 3))   # {'Olá mundo', 3, 12}
set1.discard('Olá mundo')   # {3, 12}
set1.clear()  # set()

# Operadores úteis
# união | união
# interseção & interseção
# diferença - Itens presentes apenas no set a esquerda
# diferença simétrica - itens que não estão em ambos

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 | set2  # {1, 2, 3, 4, 5}
set3 = set1 & set2  # {3}
set3 = set1 - set2  # {1, 2}
set3 = set1 ^ set2  # {1, 2, 4, 5}
