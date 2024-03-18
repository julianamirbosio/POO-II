'''10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão
no intervalo compreendido por eles.
11. Altere o programa anterior para mostrar no final a soma dos números. '''

n1, n2 = list(map(int, input("Informe dois números inteiros:").split()))

soma = 0
if n2 > n1:
    for i in range(n1,(n2-1)):
        n1 += 1
        print(n1)
        soma += n1
else:
    for i in range(n2,(n1-1)):
        n2 += 1
        print(n2)
        soma += n2
print(soma)
