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
    ab = input("Digite o arquivo para encotrarmos chaves do arquivo:")
    try:
        arq_chaves = open(ab, 'r')
    except FileNotFoundError:
        print("Arquivo não encontrado")
    else:
        chave = []
        contador = 0
        list_chaves = arq_chaves.read()
        for c in list_chaves.split(sep='|'):
            chave.append(c)
        achou = False
        arq2 = input("Digite o arquivo de saída: ")
        arq_saida = open(arq2, 'wb')
        while len(chave) > contador:
            arq.seek(0)
            registro = leia_reg(arq)
            
            while registro and achou == False:
                sobrenome = registro.split(sep='|')[0]
                
                if sobrenome == chave[contador]:
                    achou = True
                else:
                    registro = leia_reg(arq)
                print(sobrenome)
            
            

            if achou:
                    buffer = registro.encode()
                    tam = len(buffer)
                    tam_bin = tam.to_bytes(2)
                    arq_saida.write(tam_bin)
                    arq_saida.write(buffer)



            else:
                print("O campo não foi encontrado")
            contador += 1
            achou = False
       

