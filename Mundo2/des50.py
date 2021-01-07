#desafio 50: Soma dos Pares. Digite 6 números e soma somente os pares.

s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o primeiro número: '))
    if n % 2 == 0:
        s = s + n                      # s += n
        cont = cont + 1                # cont += 1
print('=>>>', end=' ')
print(f'\33[4;32mA soma dos {cont} números pares é {s}\33[m')
