#desafio 27: primeiro e último nome de uma pessoa

nome = str(input('Digite o seu nome completo: ')).strip().title().split()
print('='*40)
print(f'\33[33mO seu nome primeiro nome é \33[34m{nome[0]}')
print(f'\33[33mO seu último nome é \33[34m{nome[-1]}\33[m')
print('='*40)
