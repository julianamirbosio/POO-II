'''21. Faça um programa que peça um número inteiro e determine se ele é ou não um número
primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. 
22. Altere o programa de cálculo dos números primos, informando, caso o número não seja
primo, por quais número ele é divisível. '''

def primos(n):
    divisores = []
    for i in range(1, n+1):
        if n%i == 0:
            divisores.append(i)
    if len(divisores) == 2:
        return print("%d é um número primo" % (n))
    else:
        print("o número listado não é primo.")
        
        lista_d = list(map(str, divisores))
        lista_divisores = ', '.join(lista_d)
        resultado = f'Os divisores de {n} são: {lista_divisores}.'
        print(resultado)
    
n = int(input())
primos(n)
