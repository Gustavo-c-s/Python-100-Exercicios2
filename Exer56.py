print("""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.""")
ma = 0
mu = 0
mi = 0
me = 0
for i in range(1,5):
    p = str(input('Digite seu nome: '))
    it = int(input('Digite sua idade: '))
    s = str(input('Digite seu sexo:"F"ou "M" ')).upper()
    if i == 1:
        ma = p
        mi = it
        me = it
    else:
        me += it
        if it > mi and s == 'M':
            ma =p
        if it < 20 and s == 'F':
            mu += 1
        
print(f'O nome do homem mais velho é {ma} \nA media de idade das pessoas é de {me/4}.\nO total de mulher abaixo de 20anos é {mu}.')    