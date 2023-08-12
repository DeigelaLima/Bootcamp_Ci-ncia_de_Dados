
def main():
    
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Não é possível divisão por zero!"
   
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

if __name__ == "__main__":
    main()