#desafio 58: Jogos da advinhação V.2.0. Jogador joga até acertar, e mostre
#quantos palpites foram necessários para vencer

from random import randint
computador = randint(0, 10) #faz o computador escolher um núm. inteiro entre 0 e 10
print('\33[33m-+-' * 20)
print('\33[34mO computador pensará em um número entre 0 e 10. Tente advinhar!')
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('\33[34mQual o seu palpite: \33[m'))
    tentativas += 1
    if jogador == computador:
        acertou = True
        print('\33[1;32m**** Parabéns! Você ganhou! ****\33[m')
    else:
        if computador > jogador:
            print('\33[31mTente um número MAIOR!\33[m')
        elif computador < jogador:
            print('\33[31mTente um número MENOR!\33[m')
print(f'\33[34mForam {tentativas} tentativas até o acerto.')
print('\33[33m-+-\33[m' * 20)
