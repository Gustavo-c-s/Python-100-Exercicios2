print('Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.')

n = int(input('Digite o numero: '))

for i in range(10,0,-1):
    t = n * i
    print('{}x{}={}'.format(n,i,t))
