
###################### F U N C O E S ###################

def number_aleatorio(lim_inf, lim_sup, contador, num_escolha):
    "Descobre o número definitivo através de tentativas aleatórias entre os limites"
    num_inicial = int(randint(lim_inf, lim_sup))
    while (num_escolha != lim_inf) and (num_escolha != lim_sup):
        contador += 1
        if num_inicial in range(lim_inf, num_escolha):
            lim_inf = num_inicial
        else:
            lim_sup = num_inicial

        print(f'===== Round: {contador} ====')
        print(f'Novos limites: {lim_inf} - {lim_sup}')
        print(f'Número escolha: ',num_escolha)
        num_inicial = int(randint(lim_inf, lim_sup))
        
    fim = ' FIM '
    print(f'{fim:-^30}')
    print(f'Tentativas: ', contador)
    print(f'Número sorteado: ', num_escolha)
    record_file('Randomic', num_escolha, contador)


def number_media(lim_inf, lim_sup, contador, num_escolha):
    "Descobre o número definitivo através de tentativas executando médias entre os limites"
    num_inicial = int(abs((lim_sup - lim_inf) / 2) + lim_inf)
    while (num_escolha != lim_inf) and (num_escolha != lim_sup):
        contador += 1
        if num_inicial in range(lim_inf, num_escolha):
            lim_inf = num_inicial
        else:
            lim_sup = num_inicial

        print(f'===== Round: {contador} ====')
        print(f'Novos limites: {lim_inf} - {lim_sup}')
        print(f'Número escolha: ',num_escolha)
        num_inicial = int(abs((lim_sup - lim_inf) / 2) + lim_inf)
        
    fim = ' FIM '
    print(f'{fim:-^30}')
    print(f'Tentativas: ', contador)
    print(f'Número sorteado: ', num_escolha)
    record_file('Middle', num_escolha, contador)


def cria_header():
    arq = open('Search_numbers_results100000.csv', 'w')
    arq.write('Method' + ' , ' + 'Num_to_Find' + ' , ' + 'Attempts' + '\n')
    

def record_file(method, num_escolha, contador):
    arq = open('Search_numbers_results100000.csv', 'a')
    arq.write(str(method) +' , ' +str(num_escolha) +' , ' +str(contador) + '\n')


###################### P R O G R A M A ###################


from random import randint
cria_header()
for i in range(1, 1001):

    lim_inf = 0
    lim_sup = 100000
    contador = 0
    num_escolha = int(randint(lim_inf, lim_sup)) # Número a ser descoberto

    number_aleatorio(lim_inf, lim_sup, contador, num_escolha)
    number_media(lim_inf, lim_sup, contador, num_escolha)
