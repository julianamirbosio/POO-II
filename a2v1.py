'''2.1. Crie uma pilha padr˜ao usando orienta¸c˜ao a objetos usando um tipo
qualquer de sua preferˆencia.'''
 
class Pilha():
    def __init__(self, cpilha):
        self.cpilha = cpilha
    
    def empilhar(self, cpilha):
        pass
    
    def desempilhar():
        pass
    
mensagem = input("Bem vindo, deseja criar uma pilha: ")

if mensagem.lower() == "sim":
    print("Para encerrar o empilhamento, insira asterisco (*) ")
    
    pilha = []
    while True:
        objeto = input()
        if objeto == '*':
            print("Programa encerrado")
            break
        else:
            pilha.append(objeto)

else:
    print("Programa encerrado")
