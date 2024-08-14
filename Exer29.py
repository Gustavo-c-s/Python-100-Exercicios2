print('*escreve um programa q leia a velocidade de um carro se ele utrpassa 80km mostre q foi multado e a multa cusata 7R$ po km acima do limite*')

km = float(input('Digite a velocidade: '))
vlm = (km-80)*7
if km > 80:
    print('Você passou do limite de velocidade com {}km/h\n recebeu uma multa de R${:.2f}'.format(km,vlm))
else: 
    print('Boa Viagem!')