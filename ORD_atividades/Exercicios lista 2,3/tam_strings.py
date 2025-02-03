x = input("Digite o nome de um novo arquivo: ")
arq = open(x, 'wb')
a = input('Digite um texto para o arquivo: ')
while a != '':
    y = a.encode()
    b = len(y)
    arq.write(b.to_bytes(2))
    arq.write(a.encode())
    a = input('Digite mais um texto para o arquivo ou aperte Enter para terminar: ')
    
