def leia_reg(arq):
    try:
        tam = arq.read(2)
        tam = int.from_bytes(tam)
        if tam > 0:
            buffer = arq.read(tam)
            return buffer.decode()
        else:
            return ''
    except OSError as e:
        print(f'Erro leia campos: {e}')

x = input('Digite o nome do arquivo que você quer abrir:')
try:
    arq = open(x, 'rb')
except:
    print('erro')
else:
    chave = input('Digite o sobrenome que você busca:')
    achou = False
    registro = leia_reg(arq)
    while registro and achou == False:
        sobrenome = registro.split(sep='|')[0]
        if sobrenome == chave:
            achou = True
        else:
            registro = leia_reg(arq)

    if achou:
        n_campo = 1
        for campo in registro.split('|'):
            print(f'{n_campo}°  {campo}')
            n_campo += 1
    else:
        print("O campo não foi encontrado")

arq.close()

