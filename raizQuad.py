#Faça um Programa que receba dois números, some-os e apresente a 
#raiz quadrada do resultado.

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
    calculo = num1 + num2
    quadrado = calculo**(1/2)

    #saída
    print(f'{quadrado}')

    return 0
if __name__ == "__main__":
    main()