num = int(input('Digite um número para calcular seu fatorial: '))
contador = num
fatorial = 1
print('Calculando {}! = '.format(num), end='') #número escolhido
while contador > 0: #enquanto o contador não zerar, refazer ciclo
    print('{}'.format(contador), end='') #printa o contador a cada rodada, removendo 1
    print(' x ' if contador > 1 else ' = ', end='') #se contador for maior que 1, printa X, senão printa =
    fatorial = fatorial * contador #multiplica o fatorial pelo contador
    contador = contador - 1 #remove 1 do contador a cada rodada do 'while'.
print('{}'.format(fatorial)) #printa o resultado do fatorial x contador
