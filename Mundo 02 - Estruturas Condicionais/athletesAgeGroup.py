from datetime import datetime
print('Análise de grupo por idade')
ano = int(input('Digite o ano de nascimento: '))
hoje = datetime.now().year
if hoje - ano <= 9:
    print('Esse competidor é da categoria Mirim')
elif hoje - ano > 9 and hoje - ano <= 14:
    print('Esse competidor é da categoria Infantil')
elif hoje - ano > 14 and hoje - ano <= 19:
    print('Esse competidor é da categoria Júnior')
elif hoje - ano > 19 and hoje - ano <= 20:
    print('Esse competidor é da categoria Sênior')
elif hoje - ano > 20:
    print('Esse competidor é da categoria Master')
