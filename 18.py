'''18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o
maior valor e a soma dos valores.  '''


while True:
    try:
        num = input().split()
        for i in range(len(num)):
            num[i] = int(num[i])
        
        maior = num[0]
        menor = num[0]
        soma = 0
        
        for i in range(len(num)):
            soma += num[i]
            if num[i] > maior:
                maior = num[i]
            if num[i] < menor:
                menor = num[i]
        
        print("soma dos numeros listados é igual a %d" % (soma))
        print("%d é o menor numero da lista" % (menor))
        print("%d é o maior numero da lista" % (maior))
    except EOFError:
        break
            
