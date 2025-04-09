#Faça um Programa que receba o peso (em kg) e a altura 
#(em metros) de uma pessoa e calcule o IMC, usando a fórmula:

#IMC = peso / (altura²)

def main():
    #declaração de variável
    peso = float()
    altura = float()
    imc = float()

    #entrada de dados
    peso = float(input())
    altura = float(input())

    #processamento de dados
    imc = peso/(altura**2)

    #saída
    print(f'imc={imc:.3f}')


    return 0
if __name__ == "__main__":
    main()