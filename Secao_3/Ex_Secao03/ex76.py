# Um mini jogo aonde p o usuario irá digiitar uma palavra e dentro dessa palavra ira ser sorteado uma unica letra, que o usurario deverá advinhar qual é, caso acerte - Opção de encerrar ou continuar- Caso erre contabiliza numeros de erros e reinicia

import random
tentativas = 0
# letter_user = []

while True:
    palavra_user = str(input('Digite a palavra: '))
    letter_user = random.choice(palavra_user)
    # letter_user = [letter_aleatoria]
    
    
    letter_sort = str(input('Digite a letra que acha que foi sorteada: '))
    
    if letter_sort == letter_user:
        cont_ = str(input(f'Voce acertou, letra sorteada é: ({letter_user})!! deseja jogar novamente (SIM/NAO): ')).lower()
        
        if cont_ == 'sim':
            continue
        
        else:
            print('Obrigado por jogar, volte sempre!')
            break
        
    if letter_sort != letter_user:
        tentativas += 1
        print(f'Voce já errou {tentativas}, tente denovo!!')
        continue
        
    # elif tentativas > 1:
    #     tentativas += 1
    #     print(f'Voce já errou {tentativas}, tente denovo!!')
    #     continue

