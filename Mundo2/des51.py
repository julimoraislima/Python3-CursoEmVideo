#desafio 51: Progressão Aritmética.

print('='*40)
print(' '*10, end=' ')
print('10 TERMOS DE UMA PA')
print('='*40)
termo = int(input('Primeiro termo: '))    #termo: a partir desse número que vai fazer a progressão
razao = int(input('Razão: '))             #razão: quantas casas vai pular
decimo = termo + (10-1) * razao           #décimo: será os 10 primeiros termos
for c in range(termo, decimo + razao, razao):
    print(f'{c}', end=' ► ')
print('ACABOU')
