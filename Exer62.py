print('''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
      perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos''')

i = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
print(f'Primeiro Termo: {i}\nRazão: {r}')
cnt = 1
t = 0
m = 10 
while m !=0:   
    t+=m
    while cnt <= t: 
        print(f'{i}',end='-')
        
        i += r 
        cnt += 1
    print('FIM!')
    m = int(input('\nQntos mais vc qr q mostre? '))    