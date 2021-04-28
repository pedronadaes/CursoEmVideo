import random
print('Jo-ken-pô')
jogador = str(input('Escolha: pedra, papel ou tesoura: '))
jokenpo = ['pedra', 'papel', 'tesoura']
computador = random.choice(jokenpo)
print('Computador escolheu: {}'.format(computador))
if computador == ('pedra') and jogador == ('pedra'):
    print('Empate!')
elif computador == ('pedra') and jogador == ('tesoura'):
    print('Computador venceu!')
elif computador == ('pedra') and jogador == ('papel'):
    print('Você venceu!')
elif computador == ('tesoura') and jogador == ('tesoura'):
    print('Empate!')
elif computador == ('tesoura') and jogador == ('papel'):
    print('Computador venceu!')
elif computador == ('tesoura') and jogador == ('pedra'):
    print('Você venceu!')
elif computador == ('papel') and jogador == ('papel'):
    print('Empate!')
elif computador == ('papel') and jogador == ('pedra'):
    print('Computador venceu')
elif computador == ('papel') and jogador == ('tesoura'):
    print('Você venceu!')
