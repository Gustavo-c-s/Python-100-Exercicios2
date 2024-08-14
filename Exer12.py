print('*Leia o valor do produto e mostre com desconto de 5%*')

p = float(input('Valor do produto: '))
d = p * 0.05
np = p - d
print('O produto custa R${:.2f} com desconto de R${:.2f} ele sai a R${:.2f}.'.format(p,d,np))