#desafio 68: Jogo do Par ou Ímpar

print('=+='*35)
print('\33[7;40m** O jogador escolherá um número e se'
      ' a soma entre os dois números é Par ou Ímpar até o jogador perder **\33[m')
print('=+='*35)
from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print('\33[34mDeu Par!\33[m' if total % 2 == 0 else '\33[34mDeu Ímpar!\33[m', end=' ')
    print(f'\33[34mO computador jogou {computador} e você jogou {jogador}. Total é {total}.\33[m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\33[32mmParabéns! Você ganhou!\33[m')
            v += 1
        else:
            print('\33[31mVocê Perdeu!\33[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\33[32mParabéns! Você ganhou!\33[m')
            v += 1
        else:
            print('\33[31mVocê Perdeu!\33[m')
            break
    print('\33[7;40mVamos jogar novamente...\33[m')
print(f'\33[34mVocê venceu {v} vezes!\33[m')
