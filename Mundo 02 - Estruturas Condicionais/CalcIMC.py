print('Análise de IMC')
peso = float(input('Digite o seu peso: '))
alt = float(input('Digite sua altura: '))
imc = peso / (alt * alt)
if imc <= 18.5:
    print('Seu IMC é de {} e você está abaixo do peso'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é de {} e você está no pesso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é de {} e você está com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é de {} e você está obeso'.format(imc))
elif imc > 40:
    print('Seu IMC é de {} e você está com obesidade mórbida'.format(imc))
