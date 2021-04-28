operação = 0
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
while operação != 5:
    operação = int(input('Qual operação você deseja realizar: \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa:'))
    if operação == 1:
        print('A soma de {} + {} = {}'.format(num1, num2, num1 + num2))
    if operação == 2:
        print('O produto de {} x {} = {}'.format(num1, num2, num1 * num2))
    if operação == 3:
        if num1 > num2:
            print('O maior número entre os dois é {}'.format(num1))
        if num2 > num1:
            print('O maior número entre os dois é {}'.format(num2))
    if operação == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        operação = int(input('Qual operação você deseja realizar: \n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa:'))
print('Programa encerrado')
