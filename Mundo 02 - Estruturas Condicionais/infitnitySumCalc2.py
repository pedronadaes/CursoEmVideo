contador = soma = 0
while True:
    num = int(input('Digite um número [999 - interrompe]: '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'Você digitou {contador} números e a soma entre eles é {soma}')
