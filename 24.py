'''24. Faça um programa que calcule o mostre a média aritmética de N notas.  '''

while True:
    try:
        notas = input("Insira notas da prova: ").split()
        soma = 0
        for n in notas:
            n = float(n)
            soma += n 
        media = soma/len(notas)
        print("%.2f media final." % (media))
        
    except EOFError:
        break
