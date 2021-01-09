#desafio 55: maior e menor da sequência usando lista []

pessoas = []  #lista vazia
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    pessoas = pessoas + [peso]   #lista += [peso] #add os valores de peso na lista
print('><'*15)
print(f'\33[33m O Maior peso lido foi: {max(pessoas)}') #máximo valor da lista
print(f'\33[35m O Menor peso lido foi: {min(pessoas)}')  #mínimo valor da lista
