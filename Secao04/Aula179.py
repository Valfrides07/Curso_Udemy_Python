# Funções recursivas e recursividade (é mais viavel usar loop do que recursividade em python)

def recursividade(inicio =0, fim =10):
    if inicio >= fim:
        return fim
    
    # contador irá até chegar ao final
    inicio+=1
    return recursividade(inicio, fim)
    
print(recursividade())

