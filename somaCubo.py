#Faça um Programa que receba dois números e mostre a soma 
#dos cubos desses números dividido pela soma desses dois 
#números. A fórmula é:

#soma = (n1³ + n2³) / (n1+n2)

#Formate a saída para duas casas decimais.


def main():
    #declaração de variável
    n1 = float()
    n2 = float()
    soma = float()

    #entrada de dados
    n1 = float(input())
    n2 = float(input())

    #processamento
    soma = ((n1**3) + (n2**3)) / (n1 + n2)

    #saída
    print(f'{soma:.2f}')


    return 0
if __name__ == "__main__":
    main()