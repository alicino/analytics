
###################### F U N C T I O N S ###################

def check_number(lim_inf, lim_sup):
    "Verifica se o número sorteado é o lim_inf ou lim_sup e corrige"
    
    num_1 = int(randint(lim_inf, lim_sup)) # Número a ser descoberto
    print(f'Entrou: ', num_1)

    while (num_1 == lim_inf) or (num_1 == lim_sup):
        num_1 = int(randint(lim_inf, lim_sup)) # Número a ser descoberto
        print(f'Saiu: ',num_1)
    return num_1

###################### M A I N ###################

from random import randint

for i in range(1, 100):

    lim_inf = 1
    lim_sup = 5
    contador = 0
    #range_n = (str(lim_inf) +'_to_' +str(lim_sup))
    #num_escolha = int(randint(lim_inf, lim_sup)) # Número a ser descoberto
    num_escolha = check_number(lim_inf, lim_sup)
    print(f'Num final: ', num_escolha)
    print('- - - -')
    

