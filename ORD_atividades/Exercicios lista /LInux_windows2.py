import sys

''' Função auxiliar para gerar o nome do arquivo convertido
    a partir do nome do arquivo atual que está na lista args. 
    Retorna o nome do arquivo atual e nome do arquivo novo.'''
def gera_nomes_arqs(args) -> tuple[str, str]:
    nomeAtual = args[1]
    nomeNovo = nomeAtual.rstrip('.txt')
    opcao = args[2]
    if opcao == '-wl':
        nomeNovo += '_lin.txt'
    elif opcao == '-lw':
        nomeNovo += '_win.txt'
    return nomeAtual, nomeNovo

''' Função principal. Recebe o número de argumentos (nargs)
    e a lista de argumentos (args). '''
def main(nargs, args) -> None:
    modoDeUso = f'\nModo de uso:\n$ {args[0]} -lw|-wl nome_arq'
    # verifique se recebeu os argumentos corretamente
    if nargs < 3:
        raise Exception('Número incorreto de argumentos.'+ modoDeUso)
    if args[2] != '-wl' and args[2] != '-lw':
        raise Exception(f'O argumento {args[2]} é inválido' + modoDeUso)
    # gere os nomes dos arquivos atual e novo
    nomeAtual, nomeNovo = gera_nomes_arqs(args)
    try:
        # abra os arquivos
        arqAtual = open(nomeAtual, 'rb')
        arqNovo = open(nomeNovo, 'wb')
        # se converter de win para lin
        if args[2] == '-wl':
            while c := arqAtual.read(1):
                if int.from_bytes(c) != 13: 
                    arqNovo.write(c)
        # se converter de lin para win
        else:
            while c := arqAtual.read(1):
                if int.from_bytes(c) == 10:
                    arqNovo.write((13).to_bytes(1))
                arqNovo.write(c)
        # feche os arquivos
        arqAtual.close()
        arqNovo.close()
    except:
        print(f'Não foi possível abrir o arquivo {args[1]}')


if __name__ == '__main__':
    # chame a função main passando o número de argumentos e a lista de argumentos
    main(len(sys.argv), sys.argv)