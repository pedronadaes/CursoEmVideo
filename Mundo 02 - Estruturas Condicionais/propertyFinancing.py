print('Programa para avaliação de compra de imóvel:')
valor_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = int(input('Informe em quantos anos você deseja pagar: '))
parcela = valor_casa / (anos * 12)
print('O valor da parcela é de R${:.2f}'.format(parcela))
if parcela > (salario * 0.30):
    print('Infelizmente não é possível aprovar seu empréstimo.')
else:
    print('Seu empréstimo foi aprovado.')
