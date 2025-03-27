#Escreva um programa para ler as dimensões de um retângulo 
#(base e altura), calcular e escrever a área do retângulo.

def main():
    
    #declaraçao de variável
    a = int()
    b = int()
    area = int()
    
    #entrada de dados
    a = int(input())
    b = int(input())
    
    #processamento
    area = b*a
    
    #saída 
    print(f'{area}')
    
if __name__ == "__main__":
    main()