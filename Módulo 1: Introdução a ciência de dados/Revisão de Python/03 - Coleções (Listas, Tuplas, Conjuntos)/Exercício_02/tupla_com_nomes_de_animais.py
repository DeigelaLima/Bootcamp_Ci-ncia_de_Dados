
def main():

    animais = ("gato", "periquito", "cachorro", "leão")


    animal_informado = input("Digite um nome de um animal (Ex.: gato): ")

    if animal_informado in animais:
        print(f"O animal {animal_informado} está na lista")

    else:
        print(f"O animal {animal_informado} não está na lista")

if __name__ == "__main__":
    main()
