primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro #termo recebe o valor digitado pelo usuário
contador = 1 #contador de ciclos
total = 0 #total de termos a serem mostrados, iniciando com 0
mais = 10 #adicional de termos a serem mostrados, inicialmente 10 para começar o programa
while mais != 0: #enquanto o usuário não digitar '0', seguir com o ciclo abaixo:
    total = total + mais #adicionando o 'mais' ao 'total', o ciclo aumenta a contagem de termos
    while contador <= total: #enquanto o contador não for igual a 10, prosseguir com o ciclo.
        print('{} > '.format(termo), end='') #printa o termo e adiciona '>' após.
        termo = termo + razão #o termo passa a ser ele mesmo + a razão.
        contador = contador + 1 #adiciona mais um ao contador para finalizar os 10 ciclos de print.
    print('Pausa')
    mais = int(input('Deseja mostrar quantos termos a mais? ')) #o usuário indica quantos termos adicionais ele quer visualizar.
print('FIM')
print('Progressão finalizada com {} termos mostrados.'.format(total)) #total de termos da PA
