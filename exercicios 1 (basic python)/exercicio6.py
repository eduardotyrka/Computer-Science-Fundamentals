preco = float(input("digite o preço por kg do produto: "))
quantidade = float(input("digite o quanto você quer comprar desse produto em kg: "))

valorFinal = quantidade * preco

print(f"o preço final é {valorFinal:.2f} reais")