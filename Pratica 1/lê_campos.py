def leia_campos(arq):
    try:
        campo = ''
        verificador = arq.read(1)
        while verificador and verificador != '|':
            campo += verificador
            verificador = arq.read(1)
        return campo
    except OSError as e:
        print(f'Erro leia campos: {e}')


def main():
    nome_arq = input('Digite o nome do arquivo que você quer abrir: ')
    try:
        arq = open(nome_arq, 'r')
    except FileNotFoundError as e:
        print(f'Erro leia campos: {e}')
    else:
        campo = leia_campos(arq)
        conta_campos = 1
        concatenado = ''
        while campo:
            concatenado += (campo + '|')
            print(f'{conta_campos}. {campo}')
            campo = leia_campos(arq)
            conta_campos += 1
        print(concatenado)

if __name__ == '__main__':
    main()







    


