#Escreva um algoritmo para ler uma temperatura em graus 
#Fahrenheit, calcular e escrever o valor correspondente em 
#graus Celsius. Fórmula: c = (f-32)/1.8

def main():
    
    #declaração de variável
    temperatura = float()
    calculo = float
    
    
    #entrada de dados
    temperatura = float(input())
    
    #processamento 
    calculo = (temperatura-32)/1.8    
    
    #saída
    print(f'{calculo:.2f}')
    
    
    return 0
if __name__ == "__main__":
    main()