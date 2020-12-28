#desafio 4: dissecando uma variável

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ',type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em letra maiúscula?', a.isupper())
print('Está em minúscula?', a.islower())
print('Está capitalizado?', a.istitle())

