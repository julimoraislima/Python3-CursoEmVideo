#desafio 74: Maior e Menor valores em Tuplas- 2ª maneira

from random import sample
print('\33[36mOs números sorteados foram: ', end=' ')
a = tuple(sample(range(10), 5))
print(a)
print(f'\33[32mO maior valor é {max(a)} e o menor é {min(a)}.')
