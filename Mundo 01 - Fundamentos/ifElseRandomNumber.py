# Crie um programa que faça o computador pensar em um número entre 0 e 5 para o usuário descobrir. O programa deverá escrever na tela se o usuário acertou ou não.

import random
lista = [0, 1, 3, 4, 5] # tabém poderia ser randint(0, 5)
num1 = random.choice(lista)
num2 = int(input('Escolha um número de 0 a 5: '))
if num1 == num2:
    print('Acertou!')
else:
    print('ERROU!')
print('O número era: {}'.format(num1))
