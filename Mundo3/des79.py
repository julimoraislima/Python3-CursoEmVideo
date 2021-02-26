#desafio 79 - Valores únicos em uma Lista

valores = []
while True:
    num = int(input('Qual o valor a ser adicionado: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
        print('*'*30)
    else:
        print('Valor duplicado! Não vou adicionar.')
        print('='*30)
    r = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if r in 'N':
        break
print('+-'*20)
valores.sort()
print(f'Os valores adicionados foram {valores}')
print()
