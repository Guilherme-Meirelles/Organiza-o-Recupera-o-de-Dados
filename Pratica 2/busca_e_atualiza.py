def escrever(arq, RRN: int):
    buffer = ''
    print('Digite os dados para o novo registro')
    sobrenome = input('Digite seu sobrenome: ') +'|'
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
    buffer_64_bytes = buffer_bytes.ljust(64, b'\0')
    arq.seek(RRN * 64 +4)
    arq.write(buffer_64_bytes)

    
    



def main():
    x = input("Digite o nome do arquivo que você quer abrir:")
    try:
        
    


        try:
            arq = open(x,'r+b')
            t = arq.read(4)
            buffer = int.from_bytes(t)
            Total_Registros = buffer
        except FileNotFoundError:
            arq = open(x, 'w+b')
            # inicialize o cabeçalho e grave-o
            Total_Registros = 0
            buffer = Total_Registros.to_bytes(4)
            arq.write(buffer)
        
       
            
        verificação = True
        while verificação:
            y = int(input('''Digite a altenativa desejada:
                    1. Para inserir um registro no final.
                    2. Para reescrever um registro.
                    3. Para finalizar um programa.
                    Escolha: '''))
            if y == 1:
                escrever(arq, Total_Registros)
            
                Total_Registros += 1
                Total = Total_Registros.to_bytes(4)
                arq.seek(0)
                arq.write(Total)
                
            elif y == 2:
                RRN = int(input('Encontre o RRN desejado: '))
                arq.seek(RRN * 64 + 4)
                registro = arq.read(64).decode()
                contador = 1
                for campo in registro.split(sep = '|'):
                    print(f'{contador}° {campo}')
                    contador += 1
                escolha = int(input("Digite 1 se você quer fazer alterações no arquivo ou qualquer outra coisa se não: "))
                if escolha == 1:
                    escrever(arq, RRN)
            else:
                verificação = False
        arq.close()
        print('Operação finalizada')
    except OSError as e:
        print(f'Erro main: {e}')

if __name__ == "__main__":
    main()



