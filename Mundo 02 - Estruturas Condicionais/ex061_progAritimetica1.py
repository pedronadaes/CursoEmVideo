primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
while contador <= 10: #enquanto o contador não for igual a 10, prosseguir com o ciclo.
    print('{} > '.format(termo), end='') #printa o termo e adiciona '>' após.
    termo = termo + razão #o termo passa a ser ele mesmo + a razão.
    contador = contador + 1 #adiciona mais um ao contador para finalizar os 10 ciclos de print.
