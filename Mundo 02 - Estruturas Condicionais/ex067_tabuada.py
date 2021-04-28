num = int(input('Quer ver a tabuada de qual valor? '))
while True:
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num}x{c}={num*c}')
    num = int(input('Quer ver a tabuada de qual valor? '))
print('Programa finalizado.')
