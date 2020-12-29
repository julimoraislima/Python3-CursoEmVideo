#desafio 13: reajuste salarial

sal = float(input('Digite o salário: '))
porc = float(input('Digite a porcentagem de aumento: '))
novosal = sal + (sal * (porc/100))
print('\33[32m-\33[m'*80)
print(f'O salário de R${sal:.2f} com o aumento de {porc:.0f}% passará a ser de R${novosal:.2f}')
print('\33[32m-\33[m'*80)


