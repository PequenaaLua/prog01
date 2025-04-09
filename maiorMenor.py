#Ler dois valores numéricos inteiros e apresentar o resultado 
#da diferença do maior pelo menor valor.

def main():
    #declaração de variável
    a = int()
    b = int()
    subt = int()

    #entrada de dados
    a = int(input())
    b = int(input())

    #procesamento e saída
    if (a > b):
        subt = a - b
        print(f'{a} + {b} = {subt}')
    else:
        subt = b - a
        print(f'{b} - {a} = {subt}')

    return 0
if __name__ == "__main__":
    main()