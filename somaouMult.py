#Faça um programa que leia dois números inteiros, a e b. Se a 
#for maior que b, apresente a soma dos dois, caso a seja menor 
#ou igual a b, apresente o resultado da multiplicação dos dois. 

def main():
    #declaração de variável
    a = int()
    b = int()
    soma = int()
    mult = int()

    #entrada de dados
    a = int(input())
    b = int(input())

    #procesamento e saída
    if (a > b):
        soma = a + b
        print(f'{a} + {b} = {soma}')
    else:
        mult = a * b
        print(f'{a} x {b} = {mult}')

    return 0
if __name__ == "__main__":
    main()