import math

def main():
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * raio * raio
    print(f"A área do círculo com raio {raio} é {area:.2f}")

if __name__ == "__main__":
    main()
    