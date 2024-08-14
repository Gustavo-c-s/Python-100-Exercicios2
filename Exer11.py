print('*Leia a largura e altura de uma parede e metros,calcule sua area e a qntidade de tinta necessaria, sabendo que cada litro de tinta compre uma area de 2m²*')
a= float(input('Informe a altura da parade: '))
l=float(input('Informe a largura da parade: '))
ar= a*l
t = 2
ti = ar/t
print('A altura é {} Largura {}, sua area é de {}m² vai precisar de {} litros de tinta para pintar.' .format(a,l,ar,ti))