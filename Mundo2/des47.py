#desafio 47: contagem de pares. Mostre na tela todos os números pares de 1 a 50.

from time import sleep
for c in range(2, 51, 2): #começa no 2 que é par, vai até 50, contando de 2 em 2.
    sleep(0.3)
    print(c, end=' ')
print('Fim')
