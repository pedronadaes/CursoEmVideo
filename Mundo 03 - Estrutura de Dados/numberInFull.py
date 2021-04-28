extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = ' '
while num not in range(0,20):
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20:
        print('O número que você digitou é maior que 20, tente novamente.')
    else:
        print(f'O número que você digitou foi {extenso[num]}')
        break
print('Fim do programa.')
