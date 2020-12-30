#desafio 30: par ou ímpar

num = int(input('Digite um número inteiro: '))
print('-+-'*10)
if num % 2 == 0:
    print(f'\33[1;35mO número {num} é par.\33[m')
else:
    print(f'\33[1;31mO número {num} é ímpar.\33[m')
print('-+-'*10)

