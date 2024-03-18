'''14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares. '''

print("Informe, linha a linha, 10 quaisquer números: ")

imp = 0
par = 0
for _ in range(10):
    n = int(input())
    if (n % 2) == 0:
        par += 1
    else:
        imp += 1 
print("%i são pares" %(par))
print("%i são ímpares" %(imp))
