def main():

    NOME_ARQ = input('Digite o nome do arquivo: ')
    try:
        arq = open(NOME_ARQ,'wb')
        sobrenome = input('Digite o sobrenome ou <Enter> para sair: ')
        campo = sobrenome
        while campo:
            buffer = ''
            sobrenome += '|'
            nome = input('Digite seu nome: ') + '|'
            endereço = input('Digite seu endereço: ') + '|'
            cidade = input('Digite seu cidade: ') + '|'
            estado = input('Digite seu estado: ') + '|'
            cep = input('Digite seu cep: ') + '|'
            buffer += sobrenome
            buffer += nome 
            buffer += endereço
            buffer += cidade
            buffer += estado
            buffer += cep
            buffer_bytes = buffer.encode()
            tam = len(buffer)
            tam_bytes = tam.to_bytes(2)
            arq.write(tam_bytes)
            arq.write(buffer_bytes)
            sobrenome = input('Digite o sobrenome ou <Enter> para sair:')
            campo = sobrenome
    except:
        print('Erro')

    arq.close()
    

if __name__ == '__main__':
    main()
