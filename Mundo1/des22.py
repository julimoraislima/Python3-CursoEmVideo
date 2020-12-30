#desafio 22: analisador de texto

nome = str(input('Digite o nome completo: ')).strip().title()
print('-+'*50)
print(f'\33[31mSeu nome em maiúsculas é {nome.upper()},', end=' ')
print(f'em minúsculas é {nome.lower()},', end=' e ')
print(f'tem ao todo {len(nome)-nome.count(" ")} letras.')
nomedividido = nome.split()
print(f'\33[32mSeu primeiro nome é {nomedividido[0]} e ele tem {len(nomedividido[0])} letras.')
print(f'\33[33mSeu último nome é {nomedividido[-1]} e ele tem {len(nomedividido[-1])} letras.\33[m')
print('-+'*50)



