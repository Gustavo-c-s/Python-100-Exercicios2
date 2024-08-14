print('*Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit*')

t=float(input('Digite a Temperatura em Celsius: '))
f= (t*1.8)+32
print('Temperatura em Celsius é {:.0f}°C e Fahrenheit é {:.0f}°F'.format(t,f))