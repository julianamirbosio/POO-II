'''2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. '''

while True:
    nome = input("nome de usuario: ")
    senha = input("senha do usuario: ")
    if  nome != senha:
        print("senha valida")
        break
    else:
        while nome == senha:
            senha = input("senha invalida, insira nova senha: ")
            if senha != nome:
                print("senha valida")
                break
                
        break
