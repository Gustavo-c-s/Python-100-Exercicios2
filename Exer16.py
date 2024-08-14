import math
print('*Leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira *')

n = float(input('Digeite um valor: '))
v= math.floor(n)
print('o numero digitado foi {} aredondando ele ficou {}'.format(n,v))