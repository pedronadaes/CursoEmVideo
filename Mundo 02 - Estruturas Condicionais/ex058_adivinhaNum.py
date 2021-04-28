import random
print('Vou pensar em um número de 1 a 5, tente adivinhar!')
num = int(input('Digite o número: '))
pc = random.randint(0, 10)
palpite = 1
while num != pc:
    num = int(input('Errou, tente novamente: '))
    palpite += 1
print('Acertou! O computador pensou no número {}'.format(pc))
print('Você tentou {} vezes'.format(palpite))
