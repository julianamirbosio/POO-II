'''1.1. Implemente um algoritmo de busca binária usando orientação à
objetos em Python. '''

class Busca:
    def __init__(self, tupla):
        self.tupla = sorted(tupla)
        
    def busca_binaria(self, elemento):
        mini = 0
        maxi = len(self.tupla) - 1
        
        while mini <= maxi:
            meio = (mini + maxi) // 2
            if meio == elemento:
                return print(f'O numero buscado {elemento} está na lista na posicao {meio}')
            if meio > elemento:
                maxi = meio -1 
            else:
                mini = meio + 1
        return print(f'O numero buscado {elemento} não está na lista')

lista = input("Insira a lista de numeros: ").split() 
for i in range(len(lista)):
    lista[i] = int(lista[i])
buscado = int(input("Insira o numero a ser procurado: "))

l1 = Busca(lista)
indice = l1.busca_binaria(buscado)
