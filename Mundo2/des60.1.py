#desafio 60: Cálculo do fatorial. Mostra somente o resultado final.

ni = int(input('Digite o número para saber seu fatorial: '))
f = 1
nf = ni
while nf > 0:
    f = f * nf
    nf = nf - 1
print(f'-> O fatorial de {ni}! é {f}.')

