print(''' Crie um programa que leia vários números inteiros pelo teclado. 
      O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
      mostre quantos números foram digitados e qual foi a soma entre eles''')

c = 0
s = 0
n = 0
n = int(input('Digite um numero:[digitar o valor 999 para parar] '))
while n != 999:
    c += 1
    s += n
    n = int(input('Digite um numero:[digitar o valor 999 para para] '))
print(f'A soma dos digitos é {s} voce digitou {c} vezes.')
