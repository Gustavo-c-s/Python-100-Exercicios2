import random
print('''Faça um programa que jogue par ou ímpar com o computador. 
      O jogo só será interrompido quando o jogador perder,
     mostrando o total de vitórias consecutivas que ele conquistou no final do jogo''')

c = 0
while True:    
    pc = random.randint(0, 10)
    jo = int(input('escolhar um numero: '))
    jg = str(input('escolhar par ou impar:[P/I] ')).upper()
    n = pc+jo
    if n % 2 ==0:
        print(f'os numeros fora {pc} e {jo} soma é {n} o numero é par')
        if jg =='P':
            c+=1
            print('Você Ganhou,')
        else:
            print('Voce perdeu.')            
    else:
        print(f'os numeros fora {pc} e {jo} soma é {n} o numero é impar')
        if jg =='I':
            c+=1
            print('Você Ganhou,')
        else:
            print('Voce perdeu.')
    r = input('Você quer jogar novamente: [S/N] ').upper()
    if r =="N":
        print('Você ganhou {} vezes'.format(c))
        break 
