# Unir Listas

#def zipper(lista1, lista2):
#    
#    intervalo_maximo = min(len(lista1),len(lista2))
#    return [
#        (lista1[i],lista2[i]) for i in range(intervalo_maximo)
#    ]
 
 # Funão nativa do python
    
l1 = ['Salvador','Ubatuba,','Belo Horizonte']
l2 = ['BA','MG,','RJ']
print(list(zip(l1,l2)))