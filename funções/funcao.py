def verificarUsuario():
    nome = input("Digite seu nome: ")
   
    if nome.isdigit():
        print("Não é permitido número no nome! Tente novamente")
    else:
        print("Esse nome está disponível.")
        print("Seja bem vindo", nome)
    
    senha = input("Digite sua senha: ")
    if senha.isupper():
        print("Não é permitido letra maiúscula na senha! Tente novamente.")
        senha = input("Digite sua senha: ")
    else:
        print("Essa senha está disponível.") 
verificarUsuario()