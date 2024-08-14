print('*Mostre o numero digitado e o dobro, triplo e a raiz quadrada dele.*')
n= int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O numero digitado é {}, o dobro é {}, o triplo é {} e sua raiz quadrada é {:.3}'.format(n,d,t,r))