# Argumentos não nomeados dentro de funções, soma e subtração

while True:
    numeros = int(input('Digite o primeiro numero que deseja calcular:'))
    
    numeros_02 = int(input('Digite o segundo numero: '))
    
    pergunta_01 = str(input(f'O Primeiro numero: {numeros} está correto? [SIM/NAO]: ')).lower()
    
    pergunta_02 = str(input(f'O Segundo numero: {numeros_02} está correto? [SIM/NAO]: ')).lower()
    
    def soma(numeros, numeros_02): # Argumentos nomeados   
        calculo = numeros + numeros_02
        print(f' A soma entre {numeros} + {numeros_02} é: {calculo}')
    
    if pergunta_01 == 'nao' or pergunta_02 == 'nao':
        print('Digite novamente.')
        continue
    
    if pergunta_01 == 'sim' and pergunta_02 == 'sim':
        soma(numeros, numeros_02)
        break

    