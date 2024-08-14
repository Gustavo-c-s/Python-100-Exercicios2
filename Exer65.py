print('''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
      mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
      O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.''')

c = 0
s = 0
ma = 0
me = 0
r = ''
n = 0
while r != 'N':
    c += 1   
    n = int(input('Digite um numero: '))   
    s +=n
    if c ==1:
        ma =me =n
    else:  
        if n > ma:
            ma = n          
        if n < me:
            me = n
    r = str(input('Voce qr continuar?[S/N]: ')).upper()    
    
print(f'A media entre os numeros é de {s/c}, o maior numero foi {ma} e o menor foi {me}.')
