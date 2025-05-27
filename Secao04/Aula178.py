# Acumulador

from functools import reduce

produtos = [
    {'Nome': 'Produto 5', 'Preco': 10},
    {'Nome': 'Produto 1', 'Preco': 20},
    {'Nome': 'Produto 3', 'Preco': 4},
    {'Nome': 'Produto 2', 'Preco': 8},
    {'Nome': 'Produto 4', 'Preco': 6},
]

def funcao_do_reduce(acumulador, produto):
    print('Acumulador:', acumulador)
    print('Produto:', produto)
    print()
    return acumulador + produto['Preco']

total = reduce(
    funcao_do_reduce,
    produtos,
    0
)

print('O total:',total)