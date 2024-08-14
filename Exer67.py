print('-=-'*25)
print('''Faça um programa que mostre a tabuada de vários números, 
      um de cada vez, para cada valor digitado pelo usuário. 
      O programa será interrompido quando o número solicitado for negativo.''')
print('-=-'*25)

while True:
    n = int(input('De qual numero você qr ver a tabuada: '))
    if n <= 0:
        break
    print('='*20)   
    for c in range(1,11):
        x = n * c        
        print(f'{n}x{c}={x}')
    print('='*20)
    