#Ler quatro valores referentes a quatro notas escolares (0 a 100) 
#de um aluno e escrever uma mensagem dizendo que o aluno foi 
#APROVADO se o valor da média escolar for maior ou igual a 60, 
#Se o aluno teve média inferior a 60 e maior ou igual a 20, 
#informar que ele está de prova final, se o aluno teve media 
#inferior a 20, informar que ele está reprovado.

def main():
    #declaração de variável
    valor01 = float()
    valor02 = float()
    valor03 = float()
    valor04 = float()
    media = float()


    #entrada de dados
    valor01 = float(input())
    valor02 = float(input())
    valor03 = float(input())
    valor04 = float(input())

    #processamento e saída
    media = (valor01 + valor02 + valor03 + valor04)/4

    if (media >= 60):
        print(f'APROVADO com média {media:.2f}')
    elif(media < 60 and media >= 20):
        print(f'PROVA FINAL com média {media:.2f}')
    else:
        print(f'REPROVADO com média {media:.2f}')

    return 0
if __name__ == "__main__":
    main()