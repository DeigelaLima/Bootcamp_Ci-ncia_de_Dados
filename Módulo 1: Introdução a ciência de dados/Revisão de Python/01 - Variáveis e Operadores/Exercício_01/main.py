from operacoes_basica import soma, subtracao,multiplicacao, divisao

def main():
    
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    # Calcula e imprime os resultados
    print(f"Soma: {soma(num1, num2)}")
    print(f"Subtração: {subtracao(num1, num2)}")
    print(f"Multiplicação: {multiplicacao(num1, num2)}")
    print(f"Divisão: {divisao(num1, num2)}")

if __name__ == "__main__":
    main()