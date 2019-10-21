
###################### F U N C T I O N S ###################

def check_number(lim_inf, lim_sup):
    "Verifica se o número sorteado é o lim_inf ou lim_sup e corrige"
    
    num_1 = int(randint(lim_inf, lim_sup)) # Número inicial a ser descoberto
    print(f'** Entrou: ', num_1)

    while (num_1 == lim_inf) or (num_1 == lim_sup):
        num_1 = int(randint(lim_inf, lim_sup)) # Número CORRIGIDO a ser descoberto
        print(f'** Saiu: ', num_1)
    return num_1


def number_aleatorio(range_n, lim_inf, lim_sup, contador, num_escolha, file_name):
    "Descobre o número definitivo através de tentativas aleatórias entre os limites"
    num_inicial = int(randint(lim_inf, lim_sup))
    while (num_escolha != lim_inf) and (num_escolha != lim_sup):
        contador += 1
        if num_inicial in range(lim_inf, num_escolha):
            lim_inf = num_inicial
        else:
            lim_sup = num_inicial

        print(f'== Round: {contador} ==')
        print(f'Novos limites: {lim_inf} - {lim_sup}')
        print(f'Número escolha: ',num_escolha)
        num_inicial = int(randint(lim_inf, lim_sup))
        
    fim = ' FIM '
    print(f'Tentativas: ', contador)
    print(f'Número sorteado: ', num_escolha)
    print(f'{fim:-^30}')
    record_file(range_n, 'Randomic', num_escolha, contador, file_name)


def number_media(range_n, lim_inf, lim_sup, contador, num_escolha, file_name):
    "Descobre o número definitivo através de tentativas executando médias entre os limites"
    num_inicial = int(abs((lim_sup - lim_inf) / 2) + lim_inf)
    while (num_escolha != lim_inf) and (num_escolha != lim_sup):
        contador += 1
        if num_inicial in range(lim_inf, num_escolha):
            lim_inf = num_inicial
        else:
            lim_sup = num_inicial

        print(f'== Round: {contador} ==')
        print(f'Novos limites: {lim_inf} - {lim_sup}')
        print(f'Número escolha: ',num_escolha)
        num_inicial = int(abs((lim_sup - lim_inf) / 2) + lim_inf)
        
    fim = ' FIM '
    print(f'Tentativas: ', contador)
    print(f'Número sorteado: ', num_escolha)
    print(f'{fim:-^30}')
    record_file(range_n, 'Middle', num_escolha, contador, file_name)


def cria_header(file_name):
    arq = open(file_name, 'w')
    arq.write('Range' + ', ' + 'Method' + ', ' + 'Num_to_Find' + ', ' + 'Attempts' + '\n')
    

def record_file(range_n, method, num_escolha, contador, file_name):
    arq = open(file_name, 'a')
    arq.write(str(range_n) +', ' +str(method) +', ' +str(num_escolha) +', ' +str(contador) + '\n')

###################### M A I N ###################

from random import randint
from datetime import datetime

file_name = datetime.now().strftime("Numbers-%Y-%m-%d_%I-%M-%S_%p.csv")

cria_header(file_name)

for i in range(1, 1001):

    lim_inf = 0
    lim_sup = 100
    contador = 0
    range_n = (str(lim_inf) +'_to_' +str(lim_sup))
    num_escolha = check_number(lim_inf, lim_sup)

    number_aleatorio(range_n, lim_inf, lim_sup, contador, num_escolha, file_name)
    number_media(range_n, lim_inf, lim_sup, contador, num_escolha, file_name)

