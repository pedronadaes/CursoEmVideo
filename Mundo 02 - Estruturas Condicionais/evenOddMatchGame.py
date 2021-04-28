from random import randint
contador = 0
while True:
    jogador = int(input('Diga um número: '))
    pc = randint(0, 10)
    total = jogador + pc
    par = ' '
    while par not in 'PI':
        par = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {pc}. Total = {total}')
    if par == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            contador += 1
        else:
            print('Você perdeu!')
            break
    elif par == 'I':
        if total % 2 == 1:
            print('Você venceu')
            contador += 1
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {contador}')
