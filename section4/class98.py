'''
Os módulos do Python são Singletons, ou seja, pode haver somente uma instância dele
'''
import importlib
import class98_m

print(class98_m.variavel)

'''
Um For não funcionaria, pois não pode haver
mais de uma instância do módulo

for i in range(5):
    print(i)
    import class98_m
'''

# Podemos usar o importlib para dar um 'reload' do módulo
for i in range(5):
    importlib.reload(class98_m)
    print(i)
