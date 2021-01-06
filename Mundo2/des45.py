#desafio 45: Game-> Pedra, Papel e Tesoura.

print('==+==+== Jogo: Pedra, Papel e Tesoura. ==+==+==')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Digite sua opção: '))
if jogador >= 3:
    print('\33[31mOpção inválida. Tente novamente!!\33[m')
else:
    print('Jo')
    sleep(0.5)
    print('ken')
    sleep(0.5)
    print('Po!!')
    sleep(0.5)
    print('-='*15)
    print(f'Você jogou {itens[jogador]}')
    print(f'O Computador jogou {itens[computador]}')
    print('-='*15)
if computador == 0: #se computador jogar pedra
    if jogador == 1:
        print('->>>> Você venceu!!')
    elif jogador == 2:
        print('->>>> O computador venceu!')
if computador == 1: #se computador jogar papel
    if jogador == 0:
        print('->>>> O computador venceu!')
    elif jogador == 2:
        print('->>>> Você venceu!!')
if computador == 2: #se o computador jogar tesoura
    if jogador == 0:
        print('->>>> Você venceu!!')
    elif jogador == 1:
        print('->>>> O computador venceu!')
elif jogador == computador:
    print('->>>> Empate!!')







