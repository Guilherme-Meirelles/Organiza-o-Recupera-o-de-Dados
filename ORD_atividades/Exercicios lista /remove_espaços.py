x = input('Digite o arquivo que você quer abrir:')
arq = open(x, 'r')
y = input('Digite o nome do novo arquivo:')
arq2 = open(y, 'w')
a = arq.read(1)
arq2.write(a)
while a:
    b = a
    a = arq.read(1)
    if a != ' ' or b != ' ':
        arq2.write(a)

    



