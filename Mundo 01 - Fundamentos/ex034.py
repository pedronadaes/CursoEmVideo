salario = float(input('Digite o valor do salário: '))
if salario <= 1250.00:
    salario_final = salario * 1.15
else:
    salario_final = salario * 1.10
print('O Salário com aumento é de {:.2f}.'.format(salario_final))
