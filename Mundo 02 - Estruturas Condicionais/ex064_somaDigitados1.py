num = 0
cont = 0
soma = 0
num = int(input('Digite um número [999 interrompe o programa]: ')) #caso digite 999 aqui, interrompe o ciclo, não somando 999 ao total e aos números digitados.
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite um número [999 interrompe o programa]: '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))
