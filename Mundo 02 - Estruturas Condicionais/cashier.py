total = prod1000 = nomeprodbarato = precoprodbarato = contador = 0
while True:
    produto = str(input('Digite o produto: ')).strip().upper()
    preco = float(input('Digite o preço: R$'))
    total = total + preco
    if contador == 1 or preco < precoprodbarato:
        nomeprodbarato = produto
        precoprodbarato = preco
    if preco > 1000:
        prod1000 = prod1000 + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'S':
        contador +=1
    else:
        break
print(f'O total gasto é de R${total:.2f}')
print(f'Produtos acima de 1000 reais: {prod1000}')
print(f'O produto mais barato é {nomeprodbarato} e o valor foi R${precoprodbarato:.2f}')
