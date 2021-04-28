from datetime import datetime
print('Análise de idade para alistamento:')
ano_nascimento = int(input('Digite o ano que você nasceu: '))
hoje = datetime.now().year
if ano_nascimento + 18 == hoje:
    print('Esse ano você precisa se alistar.')
elif ano_nascimento + 18 > hoje:
    print('Não está na hora de se alistar, ainda faltam {} anos'.format((ano_nascimento + 18) - hoje))
elif ano_nascimento + 18 < hoje:
    print('Já passou da hora de se alistar, foi há {} ano(s)'.format(hoje - (ano_nascimento + 18)))
