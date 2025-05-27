# Gerador de CPF

import random

for _ in range(100):
    nove_numeros = [random.randint(0,9) for _ in range(9)]
    print(*nove_numeros)