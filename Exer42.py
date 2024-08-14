print("""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes""")

a = float(input('Digite os comprimentos: '))
b = float(input('Digite os comprimentos: '))
c = float(input('Digite os comprimentos: '))

if a+b>c and b+c>a and a+c>b:
    print('Trinagulo Formado.')  
else:
    print('Não pode forma um triangulo.')
    
if a == b and a == c:
    print('Seu triangulo é um EQUILÁTERO.')
elif a == b or b == c or a==c:
    print('Seu triangulo é uma ISÓSCELES.')
elif a != b and b != c and a != c:
    print('Seu triqangulo é um ESCALENO.')   