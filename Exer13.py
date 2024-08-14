print('*Leia o salario de um funcionario e mostre seu novo salario com um aumento de 15%*')

s = float(input('Valor do salario :'))
a = s * 0.15
ns= s + a
print('Seu salario é R${:.2f} você recebeu um aumento de R${:.2f}, agora vc recebe R${:.2f}'.format(s,a,ns))