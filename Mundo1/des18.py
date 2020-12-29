#desafio 18: seno, cosseno e tangente usando a biblioteca math do python

import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('+'*30)
print(f'\33[31mO ângulo do SENO é {seno:.2f}.')
print(f'\33[32mO ângulo do COSSENO é {cosseno:.2f}.')
print(f'\33[33mO ângulo da TANGENTE é {tangente:.2f}.\33[m')
print('+'*30)

