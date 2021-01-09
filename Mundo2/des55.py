#desafio 55: Maior e menor da sequência.

maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print('><'*15)
print(f'-> \33[34mO maior peso lido foi {maior}\33[m')
print(f'-> \33[37mO menor peso lido foi {menor}\33[m')


