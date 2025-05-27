# Funções para inverter o nome, verificar espaços existentes ou nao, quantidades de letras especificas, mostrar primeira letra e a ultima e se nada for digitado pelo usuario mostrar uma mensagem 

#Lista vazia para armazenar a qauntidade de caracteres digitados
qnt_letra = []


idade = int(input('Digite a sua idade: '))

nome = str(input('Digite o seu nome: '))
qnt_letra = len(nome)#Len para é a função para mostrar a quantidade de caracteres digitados

# .FIND é a função para selecionar qual posição do caracter desejo mostrar
primeira_letra = nome[nome.find(nome[0])]

segunda_letra = nome[nome.find(nome[-1])]


if not nome or not idade:
    print('A digitação de nome e Idade são obrigatorios.') 

# Verificação se ha ou não, espaços digitados no nome digitado 
if nome.isspace:
    print('O nome digitado contém espaços.')

elif not nome.isspace:
    print('Não contém espaços.')
    
print(f'O nome digitado é {nome} e a idade digitada é: {idade}')    
print(f'A primeira letra digitada é: {primeira_letra}')
print(f'A ultima letra digitada é: {segunda_letra}')
print(f"A quantidade de letras digitadas em nome é: {qnt_letra}")


