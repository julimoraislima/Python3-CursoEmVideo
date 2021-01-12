#desafio 60: Cálculo do fatorial. Mostra todos os números que são multiplicados.

n = int(input('Digite o número que quer saber seu fatorial: '))
c = n
f = 1
print(f'Calculando o fatorial de {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x  ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')


