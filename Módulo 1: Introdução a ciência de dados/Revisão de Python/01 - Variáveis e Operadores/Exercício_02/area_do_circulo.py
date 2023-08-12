import math

def calcula_area_do_circulo(raio):
    return math.pi * raio * raio

def main():
    raio = float(input("Digite o raio do círculo: "))
    area = calcula_area_do_circulo(raio)
    print(f"A área do círculo com raio {raio} é {area:.2f}")

if __name__ == "__main__":
    main()