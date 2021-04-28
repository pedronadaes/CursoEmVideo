somaidade = 0
media_idade = 0
homem_velho = 0
nome_velho = ''
totmulher20 = 0
for p in range(1, 5):
    print('{}ª pessoa:'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        homem_velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > homem_velho:
        homem_velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
media_idade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} e se chama {}'.format(homem_velho, nome_velho))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(totmulher20))
