'''18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o
maior valor e a soma dos valores.  

19. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''

while True:
    try:
        aceito = True
        num = input().split()
        for i in range(len(num)):
            num[i] = int(num[i])
            if num[i] < 0 or num[i] > 1000:
                aceito = False
        if aceito:
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
        else: 
            print("Insira apenas numeros entre 0 e 1000")
    except EOFError:
        break
            
