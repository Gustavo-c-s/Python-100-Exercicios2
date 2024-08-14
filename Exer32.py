print("*Faça um programa q leia im ano qualquer e mostre se é bissexto*")

ano = int(input('Digite um ano para ver se é BISSEXTO: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O {ano} é Bissexto.')
        
else:
    print(f'O {ano} não é Bissexto')