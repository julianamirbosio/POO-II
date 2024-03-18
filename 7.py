'''7. Faça um programa que leia 5 números e informe o maior número. '''

print("Informe, linha a linha, 5 quaisquer números: ")

numeros = []
for _ in range(5):
    n = int(input())
    numeros.append(n)
    
for n in numeros:
    if n > numeros[0]:
        numeros[0] = n
        
print("O maior número da contagem é %i" %numeros[0])
