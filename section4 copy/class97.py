'''
Sempre o primeiro módulo que é executado pelo python chama-se __main__
Os outros módulos tem seus próprios nomes


Aqui no exemplo, antes de importarmos de class97_m, aqui era __main__,
Agora, quando executarmos, o nome deste módulo será 'class97_m'

'''
import class97_m
from class97_m import variavel_module

# print('Este módulo é o', __name__)

# Expandindo a lista
# print(*sys.path, sep='\n')
print(class97_m.variavel_module)
print(variavel_module)
