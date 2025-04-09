#Faça um programa, em Python 3.x, que leia a massa (Kg) e a 
#força (em Newtons), submetidas sobre um corpo  e informe 
#qual é a aceleração que ele adquire;

def main():

    #declaração de variáveis
    massa = float()
    forca = float()
    formula = float()

    #entrada de dados
    massa = float(input())
    forca = float(input())

    #processamento
    formula = forca/massa

    #saída
    print(f'{formula}')


    return 0
if __name__ == "__main__":
    main()