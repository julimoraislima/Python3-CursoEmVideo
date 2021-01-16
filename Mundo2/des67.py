#desafio 67: Tabuada V.3.0- Repete a entrada até o usuário digitar um número negativo..
# Desta vez usando o while e o for in range.
print('-=-'*31)
print('\33[33m* Digite um número positivo para calcular sua tabuada ou um número negativo para finalizar *\33[m')
print('-=-'*31)
while True:
    n = int(input('Digite o número: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\33[33m{n} x {c:2} = {c * n}\33[m')
    print('-'*12)
print('\33[33mFim\33[33m')
