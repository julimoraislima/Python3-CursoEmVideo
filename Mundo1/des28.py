#desafio 28: jogo da advinhação V1.0 usando a biblioteca random/randint (computador
# escolhe um número inteiro)

from random import randint
from time import sleep
print('-+-' * 20)
print('\33[34mVou pensar em um número entre 0 e 5. Tente advinhar!\33[m')
jogador = int(input('\33[33mDigite o número que você acha que eu pensei: \33[m'))
print('-+-' * 20)
print('\33[33mProcessando...')
sleep(1)
computador = randint(0, 5) #escolhe um núm. inteiro entre 0 e 5
print(f'\33[34mO número que eu pensei foi: {computador}\33[m')
if jogador == computador:
    print('\33[32m****** Parabéns! Você ganhou! ******\33[m')
else:
    print('\33[31m------ Sinto muito, você perdeu! ------\33[m')
print('-+-' * 20)

