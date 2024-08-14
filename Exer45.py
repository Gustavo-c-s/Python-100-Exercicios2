import random
print('Crie um programa que faça o computador jogar Jokenpô com você.')
jg = ['pedra','papel','tesoura']
pc = random.choice(jg)

print('='*40)
print('Vamos jogar Jokenpô?\nEscolha entre pedra, papel e tesoura  ')
print('='*40)

ps = str(input('Informe sua jogada: ')).lower()
if ps not in jg:
    print('Algo deu errado escolha entre pedra, papel e tesoura.')
elif pc == 'pedra' and ps =='tesoura':
    print(f'Pc ganhou com {pc} e vc perdeu com {ps}.')
elif pc == 'papel' and ps =='pedra':
    print(f'Pc ganhou com {pc} e vc perdeu com {ps}.')
elif pc == 'tesoura' and ps =='papel':
    print(f'Pc ganhou com {pc} e vc perdeu com {ps}.')
elif pc == ps:
    print(f'Rolou um empate pc com {pc} e vc com {ps}.')    
else:
    print(f'Você Ganhou com {ps} e o pc perdeu com {pc}.')


