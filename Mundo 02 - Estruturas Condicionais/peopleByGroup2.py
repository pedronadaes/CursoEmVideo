pmaioridade = homens = mulher = 0
while True:
    print('Cadastre uma pessoa.')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        pmaioridade += 1
    if sexo in 'M':
        homens += 1
    if idade < 20 and sexo in 'F':
        mulher += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Pessoas com mais de 18 anos: {pmaioridade}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20: {mulher}')
