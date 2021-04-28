# programa para criar tabuada
n = int(input('Digite um número: '))
for c in range(1, 11):
    print('''{}x{} é igual:
    {}'''.format(n, c, n * c))
