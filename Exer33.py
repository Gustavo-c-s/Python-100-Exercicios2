print('**Faça um programa q leia tres numeros e mostre qual é o maior e o menor')



n1=int(input('Digite os numeros: '))
n2=int(input('Digite os numeros: '))
n3=int(input('Digite os numeros: '))
ma = n1
me = n2    

if me >= ma :
    ma = me
    me = ma
if me >= n3 :
    me = n3
if ma <= n3:
    ma = n3
if me >= n1:
    me=n1    

print(f'O numeros foram {n1}, {n2} e {n3}\nO maior é {ma} e o Menor é {me}')        
    
    
    