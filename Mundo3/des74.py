#desafio 74: Maior e Menor valores em Tuplas

from random import randint
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('\33[36mOs números sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}', end='  ')
print(f'\33[32m\nO maior número foi {max(numeros)} e o menor número foi {min(numeros)}.')
