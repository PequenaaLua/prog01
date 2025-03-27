#Escreva um algoritmo para ler o número total de eleitores de 
#um município, o número de votos brancos, nulos e válidos. 
#Calcular e escrever o percentual que cada um representa em 
#relação ao total de eleitores.

def main():
    
    #declaração de variável
    totalEleitores =  int()
    votosBrancos = int()
    votosNulos = int()
    votosValidos = int()
    brancos = float()
    nulos = float()
    validos = float()
    
    #entrada de dados
    totalEleitores =  int(input())
    votosBrancos = int(input())
    votosNulos = int(input())
    votosValidos = int(input())
    
    #processamento
    brancos = (votosBrancos/totalEleitores)*100
    nulos = (votosNulos/totalEleitores)*100
    validos = (votosValidos/totalEleitores)*100
    
    #saída
    print(f'BRANCOS={brancos:.2f} %')
    print(f'NULOS={nulos:.2f} %')
    print(f'VÁLIDOS={validos:.2f} %')
    
    return 0
if __name__ == "__main__":
    main()