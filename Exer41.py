print(""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER""")


i = int(input('Informe sua idade: '))

if i > 25 :
    print('Sua categoria é a MASTER.')

elif i > 19 :
    print('Sua categoria é a SÊNIO.')
elif i > 14 :
    print('Sua categoria é a JÚNIOR.')
    
elif i > 9 :
    print('Sua categoria é a INFANTIL.')
    
else:
    print('Sua categoria é a MIRIM.') 