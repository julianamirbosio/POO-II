'''4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa
de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.

5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada e permita repetir a operação. '''

while True:
    try:
        while True:
            a = int(input("insira a populacao do pais A: "))
            if a < 0:
                a = int(input("insira a populacao do pais A: "))
            else:
                print("populacao valida")
                break
        taxaA = float(input("insira a taxa de crescimento do pais A: "))
        taxaA = taxaA/100
        
        menor = a
        
        while True:
            b = int(input("insira a populacao do pais B: "))
            if b < 0:
                b = int(input("insira a populacao do pais B: "))
            else:
                print("populacao valida")
                break
        taxaB = float(input("insira a taxa de crescimento do pais B: "))
        taxaB = taxaB/100
        anos = 0
            
        while True:
            if anos == 0:
                print("pais A já ultrapassou a população do pais B")
                break
            if a >= b:
                print("são necessario %d anos" %(anos))
                break
            else:
                anos += 1
                a = a + a*taxaA
                b = b + b*taxaB
    except EOFError:
        break
