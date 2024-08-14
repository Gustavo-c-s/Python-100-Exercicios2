print('Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci')

n = int(input('Quantos termos quer mostrar: '))
s1 = 0
s2 = 1
co = 3
print(f'-{s1}-{s2}' ,end='')
while co <= n:
    s3 = s1 + s2
    s1 = s2
    s2 = s3
    co += 1
    print(f'-{s3}',end='')
print("-FIM!")