walking = True

while walking:

    print("Você está em uma floresta e precisa escolher um caminho para seguir.\n Você pode escolher: esquerda ou direita. (E para esquerda / D para direita)")
    caminhoLados = input()

    if caminhoLados == "E":
        print("Você encontra um rio. Você deve decidir: \natravessar ou voltar. (A para atravessar / V para voltar)")
        voltarOuNão = input()
        if voltarOuNão == "A":
            print("Você chegou a uma vila segura!")
            walking = False
        elif voltarOuNão == "V":
            print("Você volta para onde estava antes\n")
        else:
            print("Por estar indeciso você decide voltar")
    if caminhoLados == "D":
        print("Você encontra uma montanha. \nVocê deve decidir: subir ou voltar (S para subir / V para voltar)")
        voltarOuNão = input()
        if voltarOuNão == "S":
            print("Você encontrou um tesouro no topo!")
            walking = False
        elif voltarOuNão == "V":
            print("Você volta para onde estava antes\n")
        else:
            print("Por estar indeciso você decide voltar")
    else:
        print("escolha um lado")