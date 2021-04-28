# programa para somar os números pares entre 6 números
soma = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if (num % 2) == 0:
        soma = soma + num
print('A soma dos números pares é igual a {}'.format(soma))
