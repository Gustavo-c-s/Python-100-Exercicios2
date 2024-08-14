print(''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.''')
t = 0
g = 0
c = 0
b = 0
ba = ' '
print('='*30)
print('CAIXA.')
print('='*30)
while True:
    t += 1
    p = str(input("Digite o produto: "))
    v = float(input("Digite o valor: R$"))
    r =' '
    g += v
    if v > 1000:
        c += 1
    if t == 1:
        b = v
        ba = p      
    else:        
        if v < b:
            b = v
            ba = p        
    while r not in "SN":
        r = str(input("Quer acrecenta mais produtos? [S/N]:")).upper()
    if r == 'N':
        break
print('='*50)
print(f'Total gasto na compra é R${g:.2f}\n{c} acima de R$1000,00\nO produto mais barato é {ba} que custa R${b:.2f}')
print('='*50)