# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor

lista_01 =[1, 2, 3, 4, 5, 6, 7]
lista_02 = [1, 2, 3, 4]

lista_soma= []
for i in range(len(lista_02)):
    lista_soma.append(lista_01[i] + lista_02[i])
print(lista_soma)
