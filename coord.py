#Faça um programa que recebe dois pares de coordenadas e 
#calcule a distância entre os pontos. 

def main():
    #declaração de variáveis
    x1 = float()
    y1 = float()
    x2 = float()
    y2 = float()
    dist = float()


    #entrada de dados
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())

    #processamento 
    dist = (((x2 - x1)**2) + (y2 - y1)**2)**(1/2)


    #saída
    print(f'A distância entre os pontos {x1, y1} e {(x2, y2)} é {dist:.2f}.')


    return 0
if __name__ == "__main__":
    main()

