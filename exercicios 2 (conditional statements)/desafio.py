lado1 = float(input("digite o primeiro lado da da figura: "))
lado2 = float(input("digite o segundo lado da figura: "))
lado3 = float(input("digite o terceiro lado da figura: "))

if (lado1 < (lado2 + lado3)) or (lado2 < (lado1 + lado3)) or (lado3 < (lado2 + lado1)):
    print("é possível formar o triangulo!")
    if lado1 == lado2 == lado3:
        print("esse triangulo é equilatero!")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("esse triangulo é isósceles!")
    else:
        print("esse triangulo é escaleno!")
    if ((lado1 ** 2) == ((lado2 ** 2) + (lado3 ** 2))) or ((lado2 ** 2) == ((lado1 ** 2) + (lado3 ** 2))) or ((lado3 ** 2) == ((lado2 ** 2) + (lado1 ** 2))):
        print("esse triangulo é retângulo!")
    else:
        print("esse triangulo não é retangulo!")
else:
    print("não é possivel formar o triangulo!")