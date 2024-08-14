import random
print('* O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.*')
a =[]
for i in range(4):
   a.append(input('Nome do aluno: '))
   
e = random.sample(a,len(a))   

print('Os alunos q vao apresenta sao {} a ordem vai ser {}'.format(', '.join(a),', '.join(e)))

