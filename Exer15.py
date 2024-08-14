print('*Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.*')
vd = 60
vkm = 0.15
di = int(input('Quantos dias foi alugado: '))
km = float(input('Quantos KM percorreu com o carro? '))
t = (vd*di)+(vkm*km)
print('Você ficou com o carro por {} dias e percorreu um total de {}km um total a paga pelo aluguel é de R${:.2f}'.format(di,km,t))