from random import randint

lim_inf = 0
lim_sup = 1000000
contador = 0
num_escolha = int(randint(lim_inf, lim_sup)) # Número a ser descoberto

num_inicial = int(abs((lim_sup - lim_inf) / 2) + lim_inf)
# print(num_inicial)
while (num_escolha != lim_inf) and (num_escolha != lim_sup):
    contador += 1
    if num_inicial in range(lim_inf, num_escolha):
        lim_inf = num_inicial
    else:
        lim_sup = num_inicial

    print(f'===== Next round: {contador} ====')
    print(f'Novos limites: {lim_inf} - {lim_sup}')
    print(f'Número escolha: ',num_escolha)
    # print(f'Contador: ', contador)
    # num_inicial = int(randint(lim_inf, lim_sup))
    num_inicial = int(abs((lim_sup - lim_inf) / 2) + lim_inf)
    
fim = ' FIM '
print(f'{fim:-^30}')
print(f'Tentativas: ', contador)
print(f'Número sorteado: ', num_escolha)
