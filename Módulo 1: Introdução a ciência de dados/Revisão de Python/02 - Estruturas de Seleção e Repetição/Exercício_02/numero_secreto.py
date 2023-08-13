import random

def main():

    num_secreto = random.randint(1, 100)
    tentativas = 0

    print("==================================================")
    print("             JOGO DE ADIVINHAÇÃO                  ")
    print("[Procure adivinhar o número secreto entre 1 e 100]")
    print("==================================================")
   

    while True:
        print("")
        palpite = int(input("Digite o seu palpite do número secreto: "))
        tentativas += 1

        if(palpite < num_secreto):
            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print("  O número secreto é maior. Tente novamente!    ")
            print("++++++++++++++++++++++++++++++++++++++++++++++++")

        elif(palpite > num_secreto):
            print("------------------------------------------------")
            print("   O número secreto é menor. Tente novamente!   ")
            print("------------------------------------------------")
        else:
            print("")
            print("****************************************************************")
            print(f"Parabéns S2! Você acertou o número secreto {num_secreto} em {tentativas} tentativas.")
            print("****************************************************************")
            break

if __name__ == "__main__":
    main()