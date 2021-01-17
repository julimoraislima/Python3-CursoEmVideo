#desafio 69: Análise de dados do grupo.

pessoas18 = homens = mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        print('+'*40)
        if idade >= 18:
            pessoas18 += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres20 += 1
    if r == 'N':
        break
print(f'''A) {pessoas18} pessoas tem mais de 18 anos.
B) {homens} homen(s) foram cadastrados.
C) {mulheres20} mulher(es) tem menos de 20 anos.''')
