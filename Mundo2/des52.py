#desafio 52: Números primos

n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[1;32m', end=' ')
        tot = tot + 1
    else:
        print('\33[1;31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\33[mO número {n} foi divisível {tot} vezes.')
if tot == 2:
    print('Por isso ele é PRIMO.')
else:
    print('Por isso ele NÃO é primo.')

