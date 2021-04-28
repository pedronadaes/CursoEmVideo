nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))

#split divide a string em palavras, e -1 identifica o último nome antes do final