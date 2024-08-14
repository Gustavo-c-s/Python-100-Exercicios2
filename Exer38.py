print('*Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:– O primeiro valor é maior– O segundo valor é maior– Não existe valor maior, os dois são iguais*')

a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))

if a > b:
    print('O primeiro numero {} é o Maior'.format(a))
elif a == b:
    print('Não existe valor maior, os dois são iguais')
else:
    print('O segundo numero {} é o Maior'.format(b))  