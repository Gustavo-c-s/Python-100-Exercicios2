print('*Leai uma fresa e mostre qntas les "a" qual a posicao q ela aparece pela primeira vez e a ultima vez q ela aparece*')

f = str(input("Digite a frase: "))
i = f.lower()
a = f.count('a')
p = i.find('a')
u = i.find('a', -1)
print('Frase: {}\nQuantidade de Letras "A": {}\nPrimeira posiçao: {}\nUltima posiçao: {}'.format(f,a,p,u))
