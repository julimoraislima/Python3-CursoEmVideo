#desafio 70: Estatísticas em produtos

totgasto = totmil = menor = quant = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    quant += 1
    r = ' '
    if preco >= 1000.00:
        totmil += 1
    if quant == 1 or preco < menor:
        menor = preco
        barato = nome
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        totgasto = totgasto + preco
    if r == 'N':
        break
print(f'''A) Total gasto na compra: R$ \33[33m{totgasto:.2f}\33[m
B) Total de produtos custaram mais de R$ 1000.00: \33[31m{totmil}\33[m
c) O produto mais barato foi: \33[36m{barato}\33[m''')
