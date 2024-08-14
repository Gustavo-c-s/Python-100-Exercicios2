print("""*Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
      1 para binário, 2 para octal e 3 para hexadecimal.*""")

num = int(input('Digite o numero: '))

bi = bin(num)
oc = oct(num)
he = hex(num)

es = int(input('Escolha entre: 1 para binário, 2 para octal e 3 para hexadecimal para conversão.'))

if es == 1:
    print('O numero em binário: {}'.format(bi))
elif es == 2:
    print(f'O numero em Octal: {oc}')
elif es == 3:
    print(f'O numero em Hexadecimal: {he}')
