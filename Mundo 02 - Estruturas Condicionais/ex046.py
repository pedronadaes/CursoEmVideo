# programa para contagem regressiva para estouro de fogos
import time # biblioteca de controle de tempo
for c in range(10, 0, -1):
    print(c)
    time.sleep(1) # comando para o programa "dormir" por x segundos
print('BOOM!')
