#desafio 75: Análise de dados em uma Tupla

numeros = int(input('Digite o 1º valor: ')),  int(input('Digite o 2º valor: ')),\
          int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: '))
print(f'\33[32mOs valores digitados foram: {numeros}')
print(f'\33[33mO número 9 apareceu: {numeros.count(9)} vez(es).')
if 3 in numeros:
    print(f'\33[1;37mO valor 3 apareceu na posição: {numeros.index(3)+1}.')
else:
    print('\33[31mNão foi digitado nenhum valor 3.')
print('\33[35mOs valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}', end=' ')
