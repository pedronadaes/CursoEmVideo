# somar números ímpares múltiplos de 3 entre 1 e 500
s1 = 0
s2 = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        s1 = s1 + c
        s2 = s2 + 1
print('A soma de todos os {} valores ímpares e múltiplos de 3 entre 0 e 500 é igual a {}'.format(s2, s1))
