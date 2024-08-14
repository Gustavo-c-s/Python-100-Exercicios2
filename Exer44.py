print("""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros""")

pr = 500
print('O produto custa R${:.2f}'.format(pr))

fo = int(input('Informe a Forma de pagamento:\n1 - Dinheiro ou Cheque.\n2 - Vista no Cartão.\n3 - ate 2x no cartão.\n4 - 3x ou Mais no cartão.\n '))

if fo == 1:
    print('Você recebeu um desconto de 10% o produto vai sair a R${:.2f}.'.format(pr-(pr*0.1)))
elif fo == 2:
    print('Você recebeu um desconto de 5% o produto vai sair a R${:.2f}.'.format(pr-(pr*0.05)))
elif fo == 3:
    print('Não consigo da desconto produto sair a R${:.2f}.'.format(pr))
elif fo == 4:
    print('Nessa opção o produto tem um juros de 20% saindo a R${:.2f}.'.format((pr*0.2)+pr))  
else:
    print('ERROR!!\nInforme a forma de pagamento novamente.')  