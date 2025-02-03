from sys import argv
import io
# CONSTANTES
VALOR_BAIXO = ''
VALOR_ALTO = '~'
# VAR GLOBAL
numEOF = 0
def inicialize(caminho:str, numListas: int) -> tuple[list[str], list[str], list[io.TextIOWrapper], io.TextIOWrapper, bool]:
    anteriores = []
    nomes = []
    lista : list = []
    for c in range(0, numListas):
        anteriores.append(VALOR_BAIXO)
        nomes.append(VALOR_BAIXO)
        lista.append(None)
        nomearq = f'{caminho}/lista{c}.txt'
        descritor = open(nomearq, 'r')
        lista[c] = descritor
    saida = open('saida.txt', 'w')
    existem_mais_nomes = True
    return anteriores, nomes, lista, saida, existem_mais_nomes

def finalize(lista: list[io.TextIOWrapper], saida: io.TextIOWrapper, numListas: int) -> None:
    for c in range(0, numListas):
        lista[c].close()
    saida.close()

def leia_nome(lista: io.TextIOWrapper, nome_ant: str, existem_mais_nomes: bool, numListas: int) -> tuple[str, str, bool]:
    global numEOF
    nome = lista.readline()
    if lista == '':
        nome = VALOR_ALTO
        numEOF += 1
        if numEOF == numListas:
            existem_mais_nomes = False
    else:
        if nome <= nome_ant:
            ValueError("Erro de Sequencia")
    nome_ant = nome
    return nome, nome_ant, existem_mais_nomes

def kwaymerge(caminho: str, numListas: int) -> None:
    
    anteriores, nomes, lista, saida, existem_mais_nomes = inicialize(caminho, numListas)
    for c in range(0, numListas):
         nomes[c], anteriores[c], existem_mais_nomes = leia_nome(lista[c], anteriores[c], existem_mais_nomes, numListas)
    while existem_mais_nomes :
        menor = 0
        for c in range(0, numListas):
            if nomes[c] < nomes[menor]:
                menor = c
        saida.write(nomes[menor])
        nomes[menor], anteriores[menor], existem_mais_nomes = leia_nome(lista[menor], anteriores[menor], existem_mais_nomes, numListas)
    finalize(lista, saida, numListas)


def main() -> None:
    modoDeUso = f'\nModo de uso: \n$ {argv[0]} diretorio_listas num_listas'
    if len(argv) < 3:
        raise TypeError("Número incorreto de argumentos" + modoDeUso)
    kwaymerge(argv[1], int(argv[2]))

if __name__ == '__main__':
    main()