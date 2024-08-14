print("""*Crie um programa que leia duas notas de um aluno e calcule sua média,
      mostrando uma mensagem no final, de acordo com a média atingida:
      – Média abaixo de 5.0: REPROVADO– 
      Média entre 5.0 e 6.9: RECUPERAÇÃO– 
      Média 7.0 ou superior: APROVADO*""")

nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))
me = (nt1+nt2)/2

if me >= 7:
    print('APROVADO') 
elif me >= 5:
    print('RECUPERAÇAO')
else:
    print('REPROVADO')
    