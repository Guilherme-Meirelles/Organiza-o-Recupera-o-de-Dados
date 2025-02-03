arq1 = input('Digite o nome do arquivo que você quer abrir:')
arq2 = open(arq1, 'rb')
nlinhas = 0
nbytes = 0
x = arq2.read(1)
while x:
    if x == b'\n':
        nlinhas += 1
    nbytes += 1
    x = arq2.read(1)
nlinhas += 1
print(f'Há {nbytes} bytes e {nlinhas} linhas')
