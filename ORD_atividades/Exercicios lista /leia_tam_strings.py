x = input("Digite o arquivo que você quer abrir:")
arq = open(x,'rb')
tam = arq.read(2)
tam_int = int.from_bytes(tam)
while tam:
    y = arq.read(tam_int)
    z = y.decode()
    print(z)
    tam = arq.read(2)
    tam_int = int.from_bytes(tam)
    
