
'''

    Cópia Rasa - tudo que for imutável (chaves) será copiado, porém ele não entra
    em subníveis, exemplo em listas q são mutaveis. Caso eu altere o valor de
    alguma chave na CÓPIA do dicionário, o valor no dicionário copiado e o
    original serão alterados

    Deep Copy - nesse caso, importamos uma biblioteca "import copy"
    usando o módulo deepcopy(). Ex.: d2 = copy.deepcopy(d1)

    pop - apaga item com a chave especificada
    popitem - apaga último item
    update - atualiza um dict com outro

'''

person = {
    'nome': 'Pedro',
    'sobrenome': 'Pali',
    'idade': 20,
}

# Apaga a chave e retorna o valor
# apaga = person.pop('nome')  

# print(apaga)
# print(person)

person.update({
    'nome': 'Pedrin',
    'endereco': 'Av. Flores'
})

# Ou
person.update(nome='Ana')

# Ou
tupla = ('nome', 'Aninha'),
person.update(tupla)

print(person)
