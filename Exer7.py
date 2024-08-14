print('*Leia duas notas do aluno e calcuel a media*')
a = input('Nome do aluno: ')
nt1 = float(input('Primeira nota: '))
nt2 = float(input('Segunda nota: '))
m = (nt1+nt2)/2
print('O aluno {} tirou {} e {} nos teste, sua media foi de {:.2}'.format(a,nt1,nt2,m))
