'''21. Faça um programa que peça um número inteiro e determine se ele é ou não um número
primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.  '''

def primos(n):
    divisores = 0
    for i in range(1, n+1):
        if n%i == 0:
            divisores += 1
    if divisores == 2:
        return print("%d é um número primo" % (n))
    return print("o número listado não é primo")
    
n = int(input())
primos(n)
