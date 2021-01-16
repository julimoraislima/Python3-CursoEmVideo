#desafio 65: Maior e Menor Valores

r = 'S'
quant = soma = media = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    quant += 1
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / quant
print('*'*25)
print(f'\33[31mFoi digitado {quant} números e a média foi {media:.2f}')
print(f'\33[32mO maior número digitado foi {maior} e o Menor foi {menor}')

