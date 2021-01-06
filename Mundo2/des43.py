#desafio 43: Índice de Massa Corporal.

from time import sleep
peso = float(input('Digite o peso (Kg): '))
altura = float(input('Digite a altura (m): '))
imc = peso / (altura ** 2)
sleep(0.5)
print('>>>>>')
sleep(1)
print('>>>>>>>', end='')
print(f' O ICM é de {imc:.1f} e se considera: ', end='',)
if imc < 18.5:
    print('abaixo do peso.')
elif 25 > imc >= 18.5:
    print('peso ideal.')
elif 30 > imc >= 25:
    print('sobrepeso.')
elif 40 > imc >= 30:
    print('obesidade.')
else:
    print('Obesidade Morbida.')
