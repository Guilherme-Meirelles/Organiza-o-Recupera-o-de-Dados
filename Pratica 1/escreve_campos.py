def main() -> None:
    nomeArq = input('Digite o nome do arquivo a ser criado: ')
    try:
        arq = open(nomeArq, 'w')
        sobrenome = input("Digite o sobrenome ou <ENTER> para sair:\n>>>")
        # strings vazias '' retornam False no contexto do while
        while sobrenome:
            nome = input("Nome:\n>>>")
            endereco = input("Endereco:\n>>>")
            cidade = input("Cidade:\n>>>")
            estado = input("Estado:\n>>>")
            cep = input("CEP:\n>>>")
            # ---- inicio trecho 1
            arq.write(sobrenome)
            arq.write('|')
            arq.write(nome)
            arq.write('|')
            arq.write(endereco)
            arq.write('|')
            arq.write(cidade)
            arq.write('|')
            arq.write(estado)
            arq.write('|')
            arq.write(cep)
            arq.write('|')
            # ---- fim trecho 1
            # Todo o trecho 1 poderia ser substituído pela linha abaixo:
            # arq.write(f'{sobrenome}|{nome}|{endereco}|{cidade}|{estado}|{cep}|')

            sobrenome = input("Digite o sobrenome ou <ENTER> para sair:\n>>>")
        arq.close()
    except FileNotFoundError:
        print(f'Erro: Não foi possível abrir o arquivo {nomeArq}')
    except:
        print(f'Erro: Não foi possível escrever no arquivo {nomeArq}')
    
    

if __name__ == '__main__':
    main()