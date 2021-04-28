print('Progrma de conversão de números')
num = int(input('Digite o número que deseja converter: '))
convert = int(input('Você deseja converter esse número em: \n[1]Binário \n[2]Octal \n[3]Hexadecimal'))
if convert == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)))
elif convert == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)))
elif convert == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)))
else:
    print('opção inválida')
