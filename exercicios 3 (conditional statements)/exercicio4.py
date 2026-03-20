user = input("digite seu usuário: ")
password = input("digite sua senha: ")

if user == "admin":
    if password == "1234":
        print("acesso permitido!")
    else:
        print("senha incorreta!")
elif user == "convidado" and password == "":
    print("acesso restrito")
else:
    print("acesso negado!")