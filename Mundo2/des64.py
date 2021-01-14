#desafio 64: Tratando vários valores V.1.0

count = soma = 0
n = int(input('Digite um número qualquer ou 999 para sair: '))
while n != 999:
    soma = soma + n
    count = count + 1
    n = int(input('Digite um número qualquer ou 999 para sair: '))
print('~'*40)
print(f'Foram digitados \33[1;33m{count}\33[m números')
print(f'A soma entre eles é \33[1;36m{soma}\33[m')
print('~'*40)
