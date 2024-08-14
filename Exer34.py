print('leia salarios de um funcionario e calcule o aumento, se superio a 1250 calcula aumento de 10/ inferior 15/ ')

sa = float(input('Informe seu salario: '))

if sa < 1250:
    sa+=(sa*0.15)
else:
    sa+=(sa*0.1)
    
print(sa)