'''
dir - mostra todos os nomes definidos dentro uma var
ex: dir(string)
    output:['__add__', '__class__', '__contains__', '__delattr__',...]

hasattr - checar se objeto tem atributo

getattr - pegar o valor do atributo

'''

palavra = 'Ana'
metodo = 'lower'

if hasattr(palavra, 'lower'):
    print('Existe um lower')
    print(getattr(palavra, metodo)())
    print(palavra.lower())

else:
    print('Não esse o método {metodo}')

print(dir(metodo))