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