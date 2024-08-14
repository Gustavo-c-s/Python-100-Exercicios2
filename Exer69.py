print('''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.''')
print('='*30)
print('Cadastro de Pessoas.')
print('='*30)

h = 0
m = 0
mu = 0
while True:    
    no = str(input('Digite o nome: '))
    while True:
        s = str(input('Digite o sexo [M/F] : ')).upper()
        if s == 'F' or s == 'M':
            break
        else:
            print('Erro!!Digite "F" para Feminino e "M" para Masculino')  
    i = int(input('Digite a idade: '))
    if i > 18 :
        m +=1
    if s == 'F' and i < 20:
        mu += 1
    if s == 'M':
        h += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja fazer novo cadastro?[S/N]:')).upper()
    if r == 'N':
        print(f'Cadastro encerrado.\nForam cadastrados \n{m} maiores de 18 anos\n{h} Homens cadastrado\n{mu} mulheres com menos 20 anos.')
        break