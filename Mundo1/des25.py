#desafio 25: procurando uma string dentro de outra // verifica se o nome tem SILVA

nome = str(input('Digite seu nome completo: ')).strip().upper()
print('^'*30)
print(f'\33[34mSeu nome tem Silva? {"SILVA" in nome}\33[m')
print('^'*30)


