loop = True
listaNumeros = []

while loop:
    numero = int(input("digite um número: "))
    if numero != -1:
        listaNumeros.append(numero)
        print(listaNumeros)
    else:
        media = sum(listaNumeros) / len(listaNumeros)
        print(f"a média entre os números é: {media:.2}")
        loop = False