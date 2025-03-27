def main():
    
    #declaração de variável
    salarAtual = float()
    percent = float()
    novoSalar = float()
    
    #entrada de dados
    salarAtual = float(input())
    percent = float(input())
    
    #processamento
    aumento = (salarAtual * percent) / 100
    novoSalar = salarAtual + aumento
    
    #saída
    print(f'{novoSalar:.1f}')
    
if __name__ == "__main__":
    main()