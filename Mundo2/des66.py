#desafio 66: Vários números com flag. Interrompendo a repetição while com o break.

count = soma = 0
while True:
    n = int(input('Digite um número (ou 999 para parar): '))
    if n == 999:
        break
    count += 1
    soma += n
print('')
print('=>'*5, end='')
print(f' \33[33mForam digitados {count} números e a soma entre eles é {soma}')
