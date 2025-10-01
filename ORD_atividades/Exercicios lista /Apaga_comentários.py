a = input('Qual arquivo python você quer abrir:')
arq = open(a, 'r')
b = input('Digite o nome do novo arquivo:')
arq2 = open(b, 'w')
lista = arq.readlines()
for c in lista:
    x = 0
    y = True
    while y == True and x < len(c):
        if c[x] == '#':
            y = False
        x += 1
    if y == True:
        arq2.write(c)
        
print(lista)