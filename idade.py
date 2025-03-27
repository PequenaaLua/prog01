def main():
    #declaracão de variavel
    idade = int()
    meses = int()
    dias = int()
    idadDias = int()
    
    #entrada de dados
    idade = int(input())
    meses = int(input())
    dias = int(input())

    #processamento
    idadDias = (idade*365) + (meses*30) + dias
    
    #saída
    print(f'{idadDias}')
    
    return 0
if __name__ == "__main__":
    main()