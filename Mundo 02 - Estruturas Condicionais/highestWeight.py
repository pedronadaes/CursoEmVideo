# pegar o peso de 5 pessoas e identificar o maior e o menor.
list = []
for c in range(1, 6):
    peso = int(input('Digite o peso: '))
    list.append(peso) # comando para adicionar os "inputs" à lista vazia
list = sorted(list)
print('O menor peso da lista é {}'.format(list[0]))
print('O maior peso da lista é {}'.format(list[-1]))
