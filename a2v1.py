'''2.1. Crie uma pilha padrão usando orientação a objetos usando um tipo qualquer de sua preferência.'''

class Pilha:
    def __init__(self, cpilha):
        self.cpilha= cpilha 
        self.tamanho = len(cpilha)

    def mostrar(self):
        return print(self.cpilha)
      
    def empilhar(self, cobjeto): #push
        self.cpilha.append(cobjeto)

    def desempilhar(self, n): #pop
        for _ in range(n):
            self.cpilha.pop()

print("Insira, linha a linha, os itens da pilha (os primeiros estaram no fundo da pilha e os ultimos no topo): ")
print("Para encerrar o empilhamento, insira asterisco (*) ")
print()

pilha = [] #Definindo uma pilha inicial
while True:
    objeto = input()
    if objeto == '*':
        print("A sua pilha foi montada!")
        break
    else:
        pilha.append(objeto)
ppilha = Pilha(pilha)

print()
print("A qualquer momento, para consultar a pilha, digite 'pilha'. Para empilhar, digite 'empilhar'. Para desempilhar, digite 'desempilhar'. Para encerrar o programa, digite 'sair'")
print()
while True:
    comando = input()
    
    if comando == 'pilha':
        ppilha.mostrar()
      
    elif comando == 'empilhar':
        objeto = input("Insira o objeto que deseja empilhar: ")
        ppilha.empilhar(objeto)
            
    elif comando == 'desempilhar':
        num = int(input("Insira a quantidade de itens que deseja desempilhar: "))
        ppilha.desempilhar(num)
      
    elif comando == 'sair':
        print("Programa encerrado")
        break
    else:
        print("Comando inválido")
