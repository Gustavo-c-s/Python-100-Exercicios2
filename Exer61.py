print('Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.')

i = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
print(f'Primeiro Termo: {i}\nRazão: {r}')
cnt = 1
while cnt <= 10:
      
    print(i)
    i += r 
    cnt += 1