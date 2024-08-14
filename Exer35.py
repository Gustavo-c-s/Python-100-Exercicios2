print('*desenvolva um programa q leai o comprimento de tres retas e diga ao usuario se pode ou noa forma um triangulo *')

a = float(input('Digite os comprimentos: '))
b = float(input('Digite os comprimentos: '))
c = float(input('Digite os comprimentos: '))

if a+b>c and b+c>a and a+c>b:
    print('Pode forma um triangulo')
else:
    print('Não pode forma um triangulo')
    