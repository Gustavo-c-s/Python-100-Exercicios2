from datetime import datetime
print(' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.')
ano = datetime.now().year
ma = 0
me = 0

for i in range(7):
    n = int(input('Digite o ano de nascimento: '))
    if (ano - n)>18:
        ma += 1
    else:
        me += 1
print(f'Das 7 pessoas {ma} são Maior de idade e {me} são menores de idade.')        