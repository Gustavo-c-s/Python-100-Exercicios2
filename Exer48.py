print('faça um programa q calcule a somo entre todos os numeros impares que sao multiplos de tres e q se encotram entre 1 a 500')

im = 0
for c in range( 1 ,500 ):
    if c % 2 != 0 and c % 3 ==0:
        im += c
        print(im, end="-")
print('Fim')
