print('Comparador de valores')
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
elif num1 == num2:
    print('Os números {} e {} são iguais'.format(num1, num2))
