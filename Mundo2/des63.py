#desafio 63: Sequência de Fibonacci v1.0

print('>>>>>>>>>>> Sequência de Fibonacci v1.0 <<<<<<<<<<<<<<')
n = int(input('Quantos termos quer mostrar: '))
n1 = 0
n2 = 1
count = 3
print('~'*50)
print(f'  {n1} → {n2}', end=' → ')
while count <= n:
    n3 = n1 + n2
    print(f'{n3}', end=' → ')
    n1 = n2
    n2 = n3
    count += 1
print('Fim')
print('~'*50)
