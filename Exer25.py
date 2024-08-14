print('*Crie um programa q leia o nome da pessoa e se ela tem "SILVA" no nome*')

no = str(input('Digite seu nome completo: '))

tem = 'silva' in no.lower()
print(no,tem)