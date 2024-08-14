import random
print('* Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.*')
a = ['gustavo','bob','alex','max']
e= random.choice(a)
print('Entro os alunos{} vou escolhero o {} para a tarefa. '.format(a,e))