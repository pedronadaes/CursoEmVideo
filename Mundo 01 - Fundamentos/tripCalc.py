km = int(input('Digite quantos km tem a viagem: '))
if km <=200:
    print('O valor da passagem é de R${:.2f}'.format(km*0.50))
else:
    print('O valor da passagem é de R${:.2f}'.format(km*0.45))
