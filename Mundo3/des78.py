#desafio 78 - Maior e Menor Valor na Lista

numeros = list()
max = min = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite o valor na posição {n}: ')))
    if n == 0:
        max = min = numeros[n]
    else:
        if numeros[n] > max:
            max = numeros[n]
        if numeros[n] < min:
            min = numeros[n]
print(f'Você digitou os valores: {numeros}.')
print(f'O maior valor foi {max} na posição: ', end='')
for i, v in enumerate(numeros):
    if v == max:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi {min} na posição: ', end='')
for i, v in enumerate(numeros):
    if v == min:
        print(f'{i}...', end='')
print()
