print("""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida""")

al = float(input('Informe sua altura: '))
ps = float(input('Informe seu peso: '))
imc =ps//(al*al)


print('Seu IMC é = ',+ imc)
if imc > 40: 
    print('Você esta com Obesidade Mórbida.')
elif imc > 30: 
    print('Você esta com Obesidade .')
elif imc > 25: 
    print('Você esta com Sobrepeso.')
elif imc > 18.5: 
    print('Você esta com peso ideal.')
else:
    print('Você esta abaixo do peso.')