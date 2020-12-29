#desafio 10: conversor de moedas

v = float(input('Digite o valor que quer converter: R$'))
c = v / 5.49
euro = v / 6.58
yuan = v / 0.80
libra = v / 7.37
print('-'*25)
print(f'US Dollar: US${c:.2f}')
print('-'*25)
print(f'Euro: €{euro:.2f}')
print('-'*25)
print(f'Pound Sterling: £{libra:.2f}')
print('-'*25)
print(f'Yuan: Y{yuan:.2f}')
print('-'*25)
