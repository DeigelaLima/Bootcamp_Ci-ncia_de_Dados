from numero_primo import eh_primo

def main():

    numero = int(input("Digite um número inteiro: "))

    if eh_primo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")


if __name__ == "__main__":
    main()