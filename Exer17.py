import math
print('*Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa*')

co=float(input('informe o cateto oposto:'))
ca=float(input('informe o cateto adjacente:'))
hp = math.hypot(ca,co)
print('O cateto oposto é {} e o cateto adjacente é {} sua hipotenusa é {:.2f}'.format(co,ca,hp))