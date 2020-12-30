#desafio 23: separando dígitos de um número

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('='*40)
print(f'\33[31mA unidade do seu número é: {u}')
print(f'\33[32mA dezena do seu número é: {d}')
print(f'\33[33mA centena do seu número é: {c}')
print(f'\33[34mO milhar do seu número é: {m}\33[m')
print('='*40)
