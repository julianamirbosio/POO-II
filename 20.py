'''20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias
vezes e limitando o fatorial a números inteiros positivos e menores que 16. '''

def fatorial(n):
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n-1)
        
while True:
    try:
        n = int(input())
        if 0 < n < 16:
            fatn = fatorial(n)
            print(fatn)
        else:
            print("Insira apenas números inteiros positivos e menores que 16")
    except EOFError:
        break
            
