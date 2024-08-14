print('Crie um programa q mostre na tela todos os numeros pares q estao entre 1 e 50')
par = 0 
for c in range(0,50,):
    if c % 2 == 0:
       par = c 
       print(par, end ="-")
print('Fim')