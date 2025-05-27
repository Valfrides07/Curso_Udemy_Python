# Count é um iterador que é contador "Infinito"

from itertools import count
c1 = count(0, 2) # Count esta no metodo itertools
r1 = range(10)

for i in c1:
    if i > 200:
        break
    print(i)