#desafio 48: Soma de Ímpares multiplos de três. Soma de múltiplos de três de 1 até 500.

s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print('\33[35m><'*20)
print(f'A soma de todos os {cont} valores é: {s}.')
print('><'*20)

