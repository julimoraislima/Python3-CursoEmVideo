#desafio 46: contagem regressiva de 10 a 0.

from time import sleep
for c in range(10, -1, -1): #começa no 10, até o 0, contanto de -1 em -1.
    sleep(0.5)
    print(f'\33[34m{c}')
sleep(0.5)
print('\33[33mBOM')
sleep(0.5)
print('\33[31mBOM  BOM')
sleep(0.5)
print('\33[32mBOM BOM!!!!')


