#desafio 11: medida parede e quantidade de tinta

larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {area}m2.')
litro = area / 2
print(f'Voce precisará de {litro} litros de tinta para pintar essa parede.')
