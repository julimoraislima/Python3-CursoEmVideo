#desafio 38: comparando números

num1 = int(input('Digite o primeiro valor inteiro: '))
num2 = int(input('Digite o segundo valor inteiro: '))
print('\33[1;31m>>>', end=' ')
if num1 > num2:
    print('\33[1;31mO primeiro valor é maior.\33[m')
elif num2 > num1:
    print('\33[1;31mO segundo valor é maior.\33[m')
elif num1 == num2: #ou coloque somente o else:
    print('\33[1;32mNão existe valor maior, os dois são iguais!\33[m')
