vel = int(input('Digite a velocidade do carro: '))
if vel>80:
    print('Você estava acima da velocidade permitida! A multa é de R${:.2f}'.format((vel-80)*7.00))
else:
    print('Você estava dentro do limite de velocidade.')