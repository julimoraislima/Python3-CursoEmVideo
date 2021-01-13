#desafio 72: Números por extenso usando Tuplas

from time import sleep
extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', \
          'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', \
          'dezoito', 'dezenovo', 'vinte'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n <= 20:
        break
print('Pensando....')
sleep(1)
print(f'\33[35m->>>> O número digitado foi {extenso[n]}.')
