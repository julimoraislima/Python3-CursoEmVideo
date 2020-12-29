#desafio 19: sorteando um item da lista usando a biblioteca random/choice

from time import sleep
from random import choice
n1 = str(input('Digite o primeiro nome: ')).title()
n2 = str(input('Digite o segundo nome: ')).title()
n3 = str(input('Digite o terceiro nome: ')).title()
n4 = str(input('Digite o quarto nome: ')).title()
print('')
print('\33[33mSorteando...\33[m')
sleep(1)
print('>'*10, end=' ')
print(f'O nome escolhido é \33[31m{choice([n1, n2, n3, n4])}')





