#desafio 80 - Lista ordenada sem repetição

valores = []
for c in range(0, 5):
    n = int(input('Digite o valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('O valor foi adicionado na última posição...')
    else:
        pos = 0
        while pos <= len(valores): # pos é 0, então vai do 0 até o final da lista.
            if n <= valores[pos]: #verifica se o n é <= à ele, em cada posição.
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'\33[31mOs valores digitados foram {valores}')


