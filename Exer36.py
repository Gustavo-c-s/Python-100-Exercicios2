print('*Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30/ do salário ou então o empréstimo será negado*')

vlc = float(input('Informe o valor da casa: '))
sl = float(input('Informe seu salario: '))
a = int(input('Quantos anos: '))
li = sl*0.3
if vlc%a < li:
    print('NÃO APROVATO')
else:
    print('aprovato')