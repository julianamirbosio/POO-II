'''13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem. '''

base, exp = list(map(int, input("Informe base e expoente: ").split()))

resultado = 1
for _ in range(exp):
    resultado = resultado * base
print("%i elevado à %i é %i" %(base, exp, resultado))
