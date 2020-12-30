#desafio 29: radar eletrônico // calculando a multa de $7 por cada km acima do limite(80km)

veloc = float(input('Qual a velocidade atual do carro em Km/h: '))
print('=='*30)
if veloc > 80:
    multa = (veloc - 80) * 7
    print('\33[1;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h.\33[m')
    print(f'\33[1;33mVocê deverá pagar uma multa de R${multa:.2f}!\33[m')
else:
    print('\33[1;32mParabéns, você está dentro do limite de velocidade!\33[m')
print('\33[1;32mTenha um bom dia! Dirija com segurança!\33[m')
print('=='*30)
