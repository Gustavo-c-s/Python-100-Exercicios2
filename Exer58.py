import random

print('Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.')
pc = random.randint(0,10)
ac = False
pp=0
while not ac: 
    jg = int(input('Qual seu palpite: '))
    pp += 1
    if jg == pc:
        ac = True
        print(f'Você acertou, com {pp} palpites')
    else:        
        print('Você errou, tente novamente.')