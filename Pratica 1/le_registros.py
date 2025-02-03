def leia_registros(arq):
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

arq_nome = input('Digite o nome do arquivo: ')
try:
    arq = open(arq_nome, 'rb')
except FileNotFoundError as e:
    print(f'Erro {e}')
else:
    buffer = leia_registros(arq)
    conta_registro = 1
    while buffer:
        print(f'\n Registro {conta_registro} tamanho:{len(buffer)}')
        n_campo = 1
        for campo in buffer.split(sep='|'):
            
            if campo:
                print(f'{n_campo}. {campo}')
                n_campo += 1
        conta_registro += 1
        buffer = leia_registros(arq)

arq.close()




