# Um programa que peça o usuario digitar o horario e que responda ele de acordo com o horario, bom dia 0-11, boa tarde 12-17, boa noite 19-23

nome = str(input('Digite o seu nome: '))
horario = float(input('Digite o horario: '))

if horario >= 0 and horario <= 11:
    print (f'Bom dia, {nome}!')
    
elif horario >= 12 and horario <= 17:
    print (f'Boa Tarde, {nome}!')

else:
    print (f'Boa Noite, {nome}!')