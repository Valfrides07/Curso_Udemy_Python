# filter

produtos = [
    {'Nome': 'Produto 5', 'Preco': 10.00},
    {'Nome': 'Produto 1', 'Preco': 22.32},
    {'Nome': 'Produto 3', 'Preco': 10.11},
    {'Nome': 'Produto 2', 'Preco': 1005.87},
    {'Nome': 'Produto 4', 'Preco': 69.90},
]

# Modo de filtrar os preços maiores que 10
novos_produtos = [
    p for p in produtos
        if p['Preco']> 10
]

print(novos_produtos)
