arq = input('Escreva o nome do arquivo que você quer abrir:')
try:
    arq_open = open(arq, 'w')
    texto = input('Digite um texto para adicionar no arquivo:')
    arq_open.write(texto)
except:
    print('Erro')


