print('*progrma q leia o nome completo da pessoa e mostre o primeiro e o ultimo nome separados*')

no= str(input('Digite seu nome completo: '))
se = no.split()
np = se[0]
nu = se[-1]
print('Seu nome é: {}\nPrimeiro nome: {}\nUltimo nome: {}'.format(no,np,nu))