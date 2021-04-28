print('Analisador de triângulos')
r1 = float(input('Digite um valor para reta 1: '))
r2 = float(input('Digite um valor para reta 2: '))
r3 = float(input('Digite um valor para reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível montar um triângulo com essas retas.')
    if r1 == r2 == r3:
        print('Esse é um triângulo equilátero')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esse é um triângulo isósceles')
    else:
        print('Esse é um triângulo escaleno')
else:
    print('Não é possível criar um triângulo com essas retas')
