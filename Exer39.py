from datetime import datetime

print("""*Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
      se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
      do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo*""")


ano = int(input('Informe o ano de nascimento: '))
anoaa = datetime.now().year
i= anoaa-ano

if i < 18:
    print('Nao esta na hora de alistar, falta {} anos para isso'.format(18-i))
elif i == 18:
    print('Esta na hora de servi seu pais')
elif i >18:
       print('Ja passou {} anos para vc se alistar '.format(i-18)) 
elif i < 18:
    print('Nao esta na hora de alistar, falta {} anos para isso'.format(18-i))