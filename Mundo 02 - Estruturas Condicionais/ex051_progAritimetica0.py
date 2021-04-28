# ler primeiro termo e razão de uma progressão aritimética e mostras os 10 primeiros termos
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo10 = termo1 + (10 -1) * razao
for pa in range(termo1, termo10 + razao, razao):
    print(pa, end=' > ')
print('Fim.')