#desafio 77: Contando vogais em Tuplas

palavra = 'orégano', 'manjericão', 'alecrim', 'menta', 'páprica'
for p in palavra:
    print(f'\nAs vogais da palavra {p} são: ', end='')
    for vogal in p:
        if vogal.lower() in 'aáâãeéêiíoóôõuú':
            print(vogal, end=' ')
