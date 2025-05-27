# Argumentos nomeados


def soma(x,y,z=None):
    if z is not None:
        print(f'{x=}, {y=}, {z=} = ', x + y + z)
    else:
        print(f'{x=}, {y=}, {z=} = ', x + y)
        
soma(10,15,25)
soma(12,11,0)

