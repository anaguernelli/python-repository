# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
from dados import produtos
import copy


novos_produtos = [
    # list comprehension
    {**p, 'preco': round(p['preco'] * 1.10, 2)}
    for p in copy.deepcopy(produtos)
]

print(*produtos, sep='\n')

print('\n', 'Cópia profunda de produtos com preços em 10%', '\n')
print(*novos_produtos, sep='\n')


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

print('\n', 'Ordenação por nome decrescente', '\n')

produtos_ordenados_por_nome = sorted(
    novos_produtos,
    key=lambda p: p['nome'],
    reverse=True
)

# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos), key=lambda p: p['nome']
# )

print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

print('\n', 'Ordenação por preço crescente', '\n')

produtos_ordenados_por_preco = sorted(
    novos_produtos, key=lambda p: p['preco']
)

print(*produtos_ordenados_por_preco, sep='\n')


# Tentaiva 1
# def dez_porcento(produto):
#     return produto * 1.10

# for produto in produtos_copia:
#     print(f'{produto['nome']}, {dez_porcento(produto['preco']):.2f}')
#     produtos_ordenados_por_nome = sorted(produto)
