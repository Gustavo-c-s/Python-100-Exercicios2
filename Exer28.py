import random
print('*screva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu*')

pc = random.randint(0,5)
ps = int(input('Tente acerta qual o numero o pc escolheu de 0 a 5: '))

if ps == pc:
    print('MIZERAVI ACERTO!!')
else:
    print('ERROU!!\nO pc escolheu {} e vc {}'.format(pc,ps))
print('-FIM-')