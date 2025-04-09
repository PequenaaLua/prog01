#Faça um programa que receba dois números, calcule a diferença 
#entre o primeiro e o segundo, eleve o resultado da subtração 
#ao quadrado, apresente esse resultado.

def main():
    #declaração de variável
    num1 = int()
    num2 = int()
    calculo = int()
    quadrado = int()

    #entrada de dados
    num1 = int(input())
    num2 = int(input())

    #processamento
    calculo = num1 - num2
    quadrado = calculo**2

    #saída
    print(f'{quadrado}')


    return 0
if __name__ == "__main__":
    main()