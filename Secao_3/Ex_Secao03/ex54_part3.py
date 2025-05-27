# Um programa que peça o nome do usario, se ter 4 letras ou menos mostre uma mensagem 'Seu nome é curto' se tiver 5-6', Seu nome é normal' e se ter mais que 6 'Seu nome é grande' 

num_nome = []
nome = str(input('Digite o seu nome: '))
num_nome = len(nome)

if num_nome <= 4:
    print(f'O seu nome é Curto')
    
elif num_nome <= 5 and num_nome <= 6:
    print(f'O seu nome é Normal')
    
else:
    print(f'O seu nome é Grande')
