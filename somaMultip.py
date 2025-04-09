#Faça um Programa que receba três valores inteiros (a, b e c) e 
#retorne a soma de "a" e "b", multiplicado por "c"

def main():
    #declaração de variável
    a = int()
    b = int()
    c = int()
    calculo = int()

    #entrada de dados
    a = int(input())
    b = int(input())
    c = int(input())

    #processamento de dados
    calculo = (a + b) * c

    #saída
    print(f'({a} + {b} x {c} = {calculo}')

    return 0
if __name__ == "__main__":
    main()