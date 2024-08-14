print('*Pergunte a distancia de uma viagem em km, calcule o prso da passagem, cobrando 0.50 por km ate 200km e 0.45 acima de 200km*')

v = float(input('Qual o a distancia em KM da sua viagem: '))
if v > 200:
    print('Sua viagem vai custar R${:.2f}'.format(v*0.45))
else:
    print('Sua viagem vai custar R${:.2f}'.format(v*0.50))