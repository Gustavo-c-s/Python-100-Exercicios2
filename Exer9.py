print('Leia o numero e mostre a sua tabuada')

n = int(input('Digite o numero: '))

for i in range(0,11):
    t = n * i
    print('{}x{}={}'.format(n,i,t))

    