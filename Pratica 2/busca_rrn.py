x = input('Digite o nome do arquivo que você quer abrir:')
try:
    arq = open(x, 'rb')
except:
    print('erro')
else:
    cab = arq.read(4)
    total_reg = int.from_bytes(cab)
    RRN = int(input('Digite o RRN do Registro: '))
    if RRN >= total_reg:
        print('Erro')
    else:
        offset = RRN * 64 + 4
        arq.seek(offset)
        reg = arq.read(64).decode()
        for campo in reg.split(sep='|'):
            print(campo)
    arq.close()