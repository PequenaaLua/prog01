#Faça um programa que leia o raio de uma circunferência, 
#calcule e apresente a área da mesma. Considere o valor de 
# pi como 3.14159
#Formate a saída para 5 casas decimais.

def main():

    #declaração de variável
    raio = float()
    area = float()
    pi = float()

    #entrada de dados
    pi = 3.14159
    raio = float(input())

    #processamento de dados
    area = pi * (raio**2)

    #saída
    print(f'{area:.5}')


    return 0
if __name__ == "__main__":
    main()