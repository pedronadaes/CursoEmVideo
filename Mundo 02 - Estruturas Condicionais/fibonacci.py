print('SEQUÊNCIA DE FIBONACCI')
n = int(input('Quantos termos você deseja mostrar? '))
t1 = 0 #primeiro termo da sequência sempre é zero
t2 = 1 #segundo termo da sequência sempre é um
print('{} > {}'.format(t1, t2), end='') #print dos 2 primeiros termos
contador = 3 #o contador se inicia no 3 pois os 2 primeiros termos já estão definidos
while contador <= n:
    t3 = t1 + t2 #o terceiro termos é a soma dos 2 primeiros
    print(' > {}'.format(t3), end='')
    t1 = t2 #já tendo a soma, substituo o termo 1, pelo termo subsequente e assim por diante
    t2 = t3 # o mesmo de cima
    contador = contador + 1 #adicionando 1 ao contador para contar os ciclos
print(' > FIM')
