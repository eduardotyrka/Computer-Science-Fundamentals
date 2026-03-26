loop = True

while loop:
    nota = input("digite a sua nota: ")
    if 0 <= nota <= 10:
        print("nota valida!")
        loop = False
    else:
        print("digite uma nota valida!")