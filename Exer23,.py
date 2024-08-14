print('*Faça um programa q leia de um numero de 0 a 9999 e mostre na tela cada um dos digitos *')

num = (input('Digite um numero de 0 a 9999: '))
un = num[-1]
de = num[-2] if len(num) > 1 else '0'
ce = num[-3] if len(num) > 2 else '0'
mi = num[-4] if len(num) > 3 else '0'

print('Digito: {}\nUnidade: {}\nDecena: {}\nCentena: {}\nMilhar: {}'.format(num,un,de,ce,mi))
