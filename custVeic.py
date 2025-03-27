def main():
    #declaração de variável
    custCarNov = float()
    custFab = float()
    custFinal = float()
    percentDist = float()
    percentImp = float()

    #emtrada de dados
    custFab = float(input())

    #processamento
    percentDist = (custFab * 28)/ 100
    percentImp = (custFab * 45)/ 100
    custCarNov = custFab + percentImp + percentDist

    #saída de dados
    print(f'{custCarNov:.2f}')

if __name__ == "__main__":
    main()