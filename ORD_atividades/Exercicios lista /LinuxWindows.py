a = input('Qual arquivo python você quer abrir:')
arq = open(a, 'rb')
b = input('Digite o nome do novo arquivo:')
arq2 = open(b, 'wb')
c = input('Escolha a opção 1 para formato windows ou 2 para formato linux:')
x = arq.readlines()
z = len(x) - 1

if c == 1:
    for d in x[:z]:
        f = b'\r'
        e = d[:-2]
        g = e + f
        arq2.write(g)
        print(g)
        
else:
    for d in x[:z]:

        f = b'\n'
        e = d[:-2]
        g = e + f
        arq2.write(g)
        print(g)

arq2.write(x[-1])
f = b'Ola'
g = b'Viu\r'
t = f+g
print(t)





'''
while x:
    lista.append(x)
    x = arq.readline()
print(lista)
'''

