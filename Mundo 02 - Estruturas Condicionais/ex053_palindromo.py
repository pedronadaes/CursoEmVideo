#identificar palíndromos
frase = str(input('Digite uma frase: ')).strip().upper() #strip remove espaços, upper coloca tudo em maíúscula.
palavras = frase.split() #cria uma lista com as palavras da frase
tudo_junto = ''.join(palavras) #junta as palavras da lista
inverso = ''
for letra in range(len(tudo_junto) -1, -1, -1): #inverte a ordem das letras
    inverso = inverso + tudo_junto[letra]
print('O inverso de {} é {}'.format(tudo_junto, inverso))
if inverso == tudo_junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')
