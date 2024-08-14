print("""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.""")
p = 0
for i in range(0,6):
    n=int(input('informe os seis numeros: '))
    if n % 2 == 0:
       p += n 
print(f'a soma dos numeros pares é {p}')
