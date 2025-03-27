#O custo de um carro novo ao consumidor é a soma do custo de 
#fábrica com a porcentagem do distribuidor e dos impostos 
#(aplicados ao custo de fábrica). Supondo que o percentual do 
#distribuidor seja de 28% e os impostos de 45%, escrever um 
#algoritmo para ler o custo de fábrica de um carro, calcular e 
#escrever o custo final ao consumidor.

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