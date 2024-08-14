print('='*100)
print("""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.""")
print('='*100)

i = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
print(f'Primeiro Termo: {i}\nRazão: {r}')

for c in range(i,(i+10-1)*r,r):
    
    print(f'{c}', end='-> ')

