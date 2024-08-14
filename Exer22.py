print('*Crie um programa q leia o nome completo de uma pessoa e mostre  todos as letras maiusculas*')

nome =(input('Digite seu nome: '))
mi = nome.lower()
ma = nome.upper()
es = nome.split()
tl = len(''.join(es))
pn = len(es[0])
print('Seu nome: {} \nMinusculas: {}\nMaiuscula: {}\nTotal de letras: {}\nTotal de letras no primeiro nome: {}'.format(nome,mi,ma,tl,pn))