#Faça um programa que leia um número inteiro e diga 
#se ele é par ou ímpar.

def main():
    #declaração de variável
    num = int()

    #entrada de dados
    num = int(input())

    #processsamento
    if num % 2 == 0:
        print(f'{num} é PAR')
    else:
        print(f'{num} é ÍMPAR')



    return 0
if __name__ == "__main__":
    main()