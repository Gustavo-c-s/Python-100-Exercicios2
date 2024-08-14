import math
print('*Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.*')
a = float(input('Digite o angulo: '))
se = math.sin(a)
co = math.cos(a)
tan=math.tan(a)
print('Seno de {} graus: {}\nCosseno de {} graus: {}\nTangente de {} graus: {}'.format(a,se,a,co,a,tan))