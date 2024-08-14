print('Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.')

se = False

while not se:
    s = str(input('Informe seu sexo: "M" OU "S" ')).upper()
    if s == "M" or s =="S":
        se = True
        print('Sexo confirmato.')
    else:
        print('Erro!!\nDigite novamente.')