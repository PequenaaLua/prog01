#Faça um programa que leia dois números inteiros e apresente 
#o resultado de sua soma:

def main():
    
    #declaração de variável
    a = int()
    b = int()
    soma = int()
    
    #entrada de dados
    a = int(input())
    b = int(input())
    
    #processamento
    soma = a + b
    
    #saída
    print(f'{soma}')
    return 0
    
if __name__ == "__main__":
    main()