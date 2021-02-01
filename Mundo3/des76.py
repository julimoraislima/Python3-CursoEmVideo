#desafio 76: Lista de preços com Tuplas

print('+'*40)
print('{:^40}'.format('PRICE LIST'))
print('+'*40)
listagem = 'Speakers', 48.00, 'Keyboard', 42.00, 'Mouse Mat', 21.00,\
    'Headphones', 45.00, 'Mouse', 22.90, 'Laptop', 750.00
for i in listagem:
    if type(i) is str:
        print(f'\33[1;40m{i:.<30}', end='')
    if type(i) is float:
        print(f'€{i:>7.2f}\33[m')
print('+'*40)
