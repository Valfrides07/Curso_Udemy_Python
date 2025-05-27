# Uma função que vai receber via teclado um numero inteiro qualquer que vai ser somado, divido ou multiplicado utilizando a biblioteca 'import random'. Criar uma função primaria e uma secundaria que seja utilizado um decorador na segunda função '@função'

import random

# Receber nome, para no fim ser : Joao, a soma, multi, divisao dos dois numeros que voce informou esse é o resultado: 

def rece_nome():
    nome = input(str('Digite o seu nome: '))
    confirmacao = input(f' O seu nome é? {nome}, está correto?').lower()
    while True:
        try:    
            if confirmacao ==  'sim' or 's':
                print(f'Obrigado {nome} pela confirmação!')
                break
            
            else:
                nome = input(str('Digite o seu nome: '))
                
                if nome ==  'sim' or 's':
                    print(f'Obrigado {nome} pela confirmação!')
                    break
                
        except ValueError:
            erro = input('O nome digitado, está fora dos parametros estabelecidos. Por favor digite novamente.')
            
            # Verificação se o obj 'erro' faz parte de alguma classe 'float ou int'
            if isinstance(erro(float, int)):
                erro = input('O nome digitado, está fora dos parametros estabelecidos. Por favor digite novamente.')
                
            else:
                print(f'Obrigado {nome} pela confirmação!')
                break


        

# # Receber numero qualquer via teclado
# def rece_numero(num_1):
#     num_1 = input(int('Digite a sua idade: '))