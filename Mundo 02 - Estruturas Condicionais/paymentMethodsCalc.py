print('Calculadora de valores')
valor1 = float(input('Digite o valor do produto: '))
f_pag = int(input('Qual forma de pagamento: (1) Dinheiro ou cheque \n(2) Cartão à vista \n(3) Cartão em 2x \n(4) Cartão em 3x ou mais \n==>'))
if f_pag == 1:
    print('O valor é de R${:.2f}'.format(valor1 * 0.90))
elif f_pag == 2:
    print('O valor é de R${:.2f}'.format(valor1 * 0.95))
elif f_pag == 3:
    print('O valor é de R${:.2f}'.format(valor1))
elif f_pag == 4:
    print('O valor é de R${:.2f}'.format(valor1 * 1.20))
