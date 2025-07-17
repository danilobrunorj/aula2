dinheiro = True
senha = False


if dinheiro == True and senha == True:
    print("sacar")

elif dinheiro == True and senha == False:
    print("senha inválida")

elif dinheiro == False and senha == True:
    print("senha inválida")

elif dinheiro == False and senha == False:
    print("senha inválida")
