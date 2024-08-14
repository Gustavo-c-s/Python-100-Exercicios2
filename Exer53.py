n = str(input("Digite o palavra: ")).lower()
n2 = n.split()
n1 =''.join(n2)
print(n,f'\n{n1}')
inv = ''
for i in range(len(n1)-1,-1,-1):
    inv += n1[i]
if inv == n1 :
    print(f'\nA palavra "{n}" digitada é uma palíndromos')
else:
    print(f'\nA palavra "{n}" digitada não é uma palíndromos')