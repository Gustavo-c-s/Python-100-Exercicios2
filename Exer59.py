print('Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:')
n1 =int(input('Digete primeiro numero: '))
n2 =int(input('Digete segundo numero: '))
print('Oque vc quer fazer com esses numeros? ')
r = 0
while r != 5:
    
    r = int(input('''[ 1 ] somar.
[ 2 ] multiplicar.
[ 3 ] maior.
[ 4 ] novos números.
[ 5 ] sair do programa. '''))
    if r == 1:
        print(f'A soma dos numeros é {n1+n2}')
    if r == 2:
        print(f'A mutiplicaçao dos numeros é {n1*n2}')
    if r  == 3 :
        if n1>n2:
            print(f'O maioe é {n1}.')
        else:
            print(f'O maioe é {n2}.')    
    if r == 4:
        n1 =int(input('Digete primeiro numero: '))
        n2 =int(input('Digete segundo numero: '))
        print('Oque vc quer fazer com esses numeros? ')  
    if r == 5:
        print('At mais.')
