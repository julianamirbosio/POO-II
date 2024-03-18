'''10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão
no intervalo compreendido por eles. '''

n1, n2 = list(map(int, input("Informe dois números inteiros:").split()))

if n2 > n1:
    for i in range(n1,(n2-1)):
        n1 += 1
        print(n1)
else:
    for i in range(n2,(n1-1)):
        n2 += 1
        print(n2)
