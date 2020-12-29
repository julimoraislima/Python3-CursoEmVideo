#desafio 17: catetos e hipotenusas usando matemática

co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hipo = (co**2 + ca**2)**(1/2)
print('='*30)
print(f'A hipotenusa vai medir {hipo:.2f}')
print('='*30)

