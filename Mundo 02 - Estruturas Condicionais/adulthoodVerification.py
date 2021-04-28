# identificar maior idade da pessoa com base no ano de nascimento
from datetime import datetime
soma1 = 0
soma2 = 0
ano_hoje = datetime.now().year
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento: '))
    if ano_hoje - ano >= 18:
        soma1 = soma1 + 1
    elif ano_hoje - ano < 18:
        soma2 = soma2 + 1
print('{} pessoas já atingiram a maior idade.'.format(soma1))
print('{} pessoas ainda não atingiram a maior idade'.format(soma2))
