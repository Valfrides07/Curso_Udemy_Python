# Um programa que peça para o usuario digitar um numero inteiro e informe se é impar ou par, caso o numero nao seja inteiro, informe que não é

try:
    par_impar = int(input('Digite um numero: '))

    vef_numero = par_impar % 2  

    if vef_numero == 0:
        print('O numero é Par')
    else:
        print('O numero é Impar')
        
except ValueError:
    print('O valor digitado não é do tipo inteiro')