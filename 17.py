'''17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120 '''

def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n-1)
        
n = int(input())
fatn = fatorial(n)
print(fatn)
