print('*Crie um programa q leia o nome da ciadade e se ela comeca ou nao com "santos"*')

ci =str(input("Digite sua cidade: "))
co = ci.lower()
ce = co.split()
tem = 'santos' in ce[0]
print(ci,co,ce,tem)