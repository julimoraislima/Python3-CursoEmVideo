#desafio 20: sorteando uma ordem na lista usando a biblioteca random/sample

from random import sample
n1 = str(input('Primeiro nome: ')).title()
n2 = str(input('Segundo nome: ')).title()
n3 = str(input('Terceiro nome: ')).title()
n4 = str(input('Quarto nome: ')).title()
lista = [n1, n2, n3, n4]
print('='*90)
print(f'A ordem de apresentação do trabalho será:\33[33m {sample(lista, k=4)}\33[m')
print('='*90)
