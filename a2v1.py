'''2.1. Crie uma pilha padrão usando orientação a objetos usando um tipo qualquer de sua preferência.'''

class Pilha:
    def __init__(self, cpilha):
        self.cpilha= cpilha 
        tamanho = len(cpilha)

    def empilhar(self, cobjeto): #push
        self.cpilha = self.cpilha.append(cobjeto)

    def desempilhar(self, cobjeto): #pop
        for i

print("Insira, linha a linha, os itens da pilha (os primeiros estaram no fundo da pilha e os ultimos no topo): ")
print("Para encerrar o empilhamento, insira asterisco (*) ")
print()

pilha = [] #Definindo uma pilha inicial
while True:
    objeto = input()
    if objeto == '*':
        print("Programa encerrado")
        break
    else:
        pilha.append(objeto)
ppilha = Pilha(pilha)

while True:
  print("A qualquer momento, para consultar a pilha, digite 'pilha'. Para empilhar, digite 'empilhar'. Para desempilhar, digite 'desempilhar'. Para encerrar o programa, digite 'sair'")
  print()
  comando = input()
  
  if comando == 'pilha':
      print(ppilha)
    
  elif comando == 'empilhar':
      objeto = input("Insira o objeto que deseja empilhar: ")
      ppilha.empilhar(objeto)
          
  elif comando == 'desempilhar':
    
  elif comando == 'sair':
      print("Programa encerrado")
      break
        else:
            pilha.append(objeto)

else:
    print("Programa encerrado")
