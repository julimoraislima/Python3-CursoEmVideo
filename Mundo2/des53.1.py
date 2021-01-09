#desafio 53: Detector de Palíndromo (uma frase que dá para ler ao contrário)
#ex: A sacada da casa. // Sem usar o FOR in range

frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]  #:de onde começa, :de onde termina, -1 contando de trás p frente
print(f'A frase digitada é {junto} e seu inverso é {inverso}.')
if inverso == junto:
    print('-> Portanto é um Palíndromo!')
else:
    print('-> Portanto NÃO é um Palíndromo!')

