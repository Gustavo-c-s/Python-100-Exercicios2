print('Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos')
ma = 0
me = 0

for i in range(1,6):
    p = float(input('Digite seu peso: '))
    if i == 1:
        me = p
        ma = p
    else:
        if p > ma:
            ma =p
        if p < me:
            me = p
print(f'O maior peso é {ma}.\nO menor peso é {me}.')    
     