loop = 1

pares = []
impares = []

while loop <= 10:
    numero = int(input("digite um número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    loop += 1

print(f"você digitou {len(pares)} números pares")
print(f"você digitou {len(impares)} números impares")