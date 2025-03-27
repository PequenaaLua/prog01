#Faça um programa que leia dois números inteiros e apresente o 
#resultado da multiplicação de um pelo outro:

def main():
    
    #declaração de variáveis
    a = int()
    b = int()
    mult = int()
    
    #entrada de dados
    a = int(input())
    b = int(input())
    
    #processamento
    mult = a*b
    
    #saída de dados
    print(f'{mult}')
    
    
    return 0
if __name__ == "__main__":
    main()