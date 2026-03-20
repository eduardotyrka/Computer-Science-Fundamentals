cordenadaX = input("digite a cordenada x do ponnto")
cordenadaY = input("digite a cordenada y do ponnto")

if 0 < cordenadaX < 10 and 0 < cordenadaY < 10:
    print("o ponto está dentro do quadrado!")
elif ((cordenadaX == 10 or cordenadaX == 0) and 0 <= cordenadaY <= 10) or ((cordenadaY == 10 or cordenadaY == 0) and 0 <= cordenadaX <= 10):
    print("o ponto está na fronteira!")
else:
    print("o ponto está fora do quadrado!")