#desafio 16: usando o trunc, o trunc quebra o número real deixando ele inteiro.

from math import trunc
num = float(input('Digite um número real: '))
print('='*40)
print(f'O número {num} tem a parte inteira {trunc(num)}')
print('='*40)
