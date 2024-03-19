'''23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele
executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o
número de testes (divisões) executados '''

def primos(n):
    for i in range(1, a+1):
        lista_primos = []
        divisores = []
        div = 0
        for i in range(1, n+1):
            if n%i == 0:
                divisores.append(i)
                div += 1
        if len(divisores) == 2:
            lista_primos.append(n)
    return:
        div
        
        
     
    lista_p = list(map(str, lista_primos))
    primos = ', '.join(lista_p)
    print(primos)
        
a = int(input())
for i in range(1, a+1):
    primos(i)
    
