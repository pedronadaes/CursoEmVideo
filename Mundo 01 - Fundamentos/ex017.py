import math
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hi))
