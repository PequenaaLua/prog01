#Escreva um programa para ler um valor INTEIRO (do teclado) e 
#escrever (na tela) o seu antecessor.

def main():
    
    #declaração de variáveis
    a = int()
    ant = int()
    
    #entrada de dados
    a = int(input())
    
    #processamento
    ant = a - 1
    
    #saída
    print(f'{ant}')
    
    return 0
if __name__ == "__main__":
    main()