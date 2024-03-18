'''8. Faça um programa que leia 5 números e informe a soma e a média dos números. '''
print("Informe, linha a linha, 5 quaisquer números: ")

numeros = []
for _ in range(5):
    n = int(input())
    numeros.append(n)

soma = 0
divisor = 0    
for n in numeros:
    soma += n
    divisor += 1

media = soma // divisor
        
print("A soma é %i e a média é %i" %(soma, media))
