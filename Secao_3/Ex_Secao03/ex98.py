# Cálculo do primeiro dígito do CPF
 
cpf = '746824890'
converter = int(cpf)

nove_digitos = cpf[:9]
contador_ = 10

resultado_geral = 0
for numero in nove_digitos:
    resultado_geral += int(numero) * contador_
    contador_ -=1
    primeiro_digito = (resultado_geral*10) % 11

    print(numero,'x', contador_,':', int(numero) * contador_ )
    maior_nove = primeiro_digito if primeiro_digito > 9 else 0
print('Digito final: ',primeiro_digito)
