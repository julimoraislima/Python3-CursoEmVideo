#desafio 17: catetos e hipotenusas, usando a biblioteca math do python.

import math
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hipo = math.hypot(co, ca)
print('\33[33m-\33[m'*40)
print(f'\33[35mA hipotenusa vai medir {hipo:.2f}\33[m')
print('\33[33m-\33[m'*40)

