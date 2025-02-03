x = input("Digite o arquivo que você quer abrir: ")
arq = open(x, 'rb')
y = arq.read(4)
while y:
    print(int.from_bytes(y))
    y = arq.read(4)