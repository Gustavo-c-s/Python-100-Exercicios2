print("Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.")

n = int(input('Informe o número: '))
c = 0
for i in range(1,n +1):
    if n % i == 0:
        c += 1
if c > 2:
    print(f'O numero {n} foi divisivel {c} vezes, não é primo.')
else:
    print(f'O numero {n} foi divisivel {c} vezes, ele é primo.')
  