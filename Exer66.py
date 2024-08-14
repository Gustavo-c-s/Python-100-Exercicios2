print(''' Crie um programa que leia vários números inteiros pelo teclado. 
      O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
      mostre quantos números foram digitados e qual foi a soma entre eles''')

c = 0
s = 0
while True:   
    n = int(input('Digite um numero:[digitar o valor 999 para parar] '))    
    if n == 999:       
        break
    c += 1
    s += n
print(f'A soma dos digitos é {s} voce digitou {c} vezes.')
