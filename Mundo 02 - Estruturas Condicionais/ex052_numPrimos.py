# programa para identificar se o número é primo
num = int(input('Digite um número: '))
tot = 0 #total de divisores do número
for c in range(1, num +1):
    if num % c == 0:
        print('\033[34m', end=' ') #código de cor, 34 = azul
        tot += 1
    else:
        print('\033[31m', end=' ') #código de cor, 31 = vermelho
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2: #se o total de divisores for 2, o núm é primo
    print('Por isso é um número PRIMO.')
else:
    print('Por isso ele não é um número PRIMO.')
